#!/usr/bin/env python3
import argparse
import numpy as np


def parseArguments():
    ap = argparse.ArgumentParser()
    ap.add_argument("-c", "--coin", required=True,
                    help="coin to display (example: bitcoin)")
    ap.add_argument("-b", "--base", required=True,
                    help="base currency (example: usd)")
    ap.add_argument("-d", "--days", required=True,
                    help="days ago (inputs: 1/7/14/30/90/180/365)")
    ap.add_argument("-x", "--hlim", required=False,
                    help="height of the terminal box", default=60, type=int)
    ap.add_argument("-y", "--vlim", required=False,
                    help="width of the terminal box", default=30, type=int)
    args = vars(ap.parse_args())

    return args


def findBox(highc, lowc, timec, hlim, vlim):
    tSpan = timec[len(timec) - 1] - timec[1]
    tJump = timec[1] - timec[0]
    yMax = max(highc)
    yMin = min(lowc)
    priceSpan = yMax - yMin

    candlesJump = len(timec)//hlim
    if (((len(timec) - 1)//hlim)) < 1:
        maxWidth = len(timec) - 1
        print(f"maximum width is {maxWidth} due to APIs data sizing")
        print(f"add or modify -x or --hlim value to {maxWidth}")
        exit()

    candlesSkip = len(timec) - (hlim*candlesJump)
    priceJump = float(priceSpan)/vlim
    return candlesJump, priceJump, tSpan, yMax, yMin, tJump, candlesSkip


def numberMatrix(openc, highc, lowc, closec, candlesJump, priceJump,
                 yMax, candlesSkip, hlim, vlim):

    # Allocating memory
    inThaMatrix = np.zeros((hlim, vlim), dtype=int)

    for i in range(hlim):
        openCandle = openc[i*candlesJump + candlesSkip]
        closeCandle = closec[(i+1)*candlesJump - 1 + candlesSkip]
        lowCandle = min(lowc[(i*candlesJump + candlesSkip)
                        :((i+1)*candlesJump + candlesSkip)])
        highCandle = max(highc[(i*candlesJump + candlesSkip):
                               ((i+1)*candlesJump + candlesSkip)])

        for j in range(vlim):
            rangeDown = yMax - (j+1)*priceJump

            if openCandle > closeCandle:
                if highCandle > rangeDown:
                    inThaMatrix[i, j] = 1
                if openCandle > rangeDown:
                    inThaMatrix[i, j] = 2
                if closeCandle > rangeDown:
                    inThaMatrix[i, j] = 1
                if lowCandle > rangeDown:
                    inThaMatrix[i, j] = 1
                    break

            if closeCandle > openCandle:
                if highCandle > rangeDown:
                    inThaMatrix[i, j] = 3
                if closeCandle > rangeDown:
                    inThaMatrix[i, j] = 4
                if openCandle > rangeDown:
                    inThaMatrix[i, j] = 3
                if lowCandle > rangeDown:
                    inThaMatrix[i, j] = 3
                    break
    return inThaMatrix


def printLines(numberMatrix, hlim, vlim, priceJump, yMax, currency, tJump, candlesJump, actualPrice, baseCurrency):
    formatTime = float(tJump)/1000*candlesJump
    if formatTime < 60:
        formatTime = str(round(formatTime, 2)) + " s"
    elif formatTime >= 60 and formatTime < 3600:
        formatTime = formatTime/60
        formatTime = str(round(formatTime, 2)) + " min"
    elif formatTime >= 3600 and formatTime < 3600*24:
        formatTime = formatTime/3600
        formatTime = str(round(formatTime, 2)) + " hours"
    elif formatTime >= 3600*24 and formatTime < 3600*24*30:
        formatTime = formatTime/(3600*24)
        formatTime = str(round(formatTime, 2)) + " days"
    elif formatTime >= 3600*24*30:
        formatTime = formatTime/(3600*24*30)
        formatTime = str(round(formatTime, 2)) + " months"

    headerStr = "\033[34m■\033[0m \033[01m" + currency.capitalize() + " Chart   \033[35m■\033[0m \033[01m Time Format: " + formatTime + \
        "   \033[36m■\033[0m \033[01m Actual Price: " + \
        str(round(actualPrice, 2)) + " " + baseCurrency
    print(" \n")
    print("          " + headerStr)
    print('\033[0m' + " ")
    for i in range(vlim):
        line = " "
        for j in range(hlim):
            if numberMatrix[j, i] == 2:
                format = ';'.join([str(1), str(35), str(40)])
                line += '\x1b[%sm %s \x1b[0m' % (format, "█")
            elif numberMatrix[j, i] == 1:
                format = ';'.join([str(1), str(35), str(40)])
                line += '\x1b[%sm %s \x1b[0m' % (format, "│")
            elif numberMatrix[j, i] == 3:
                format = ';'.join([str(1), str(32), str(40)])
                line += '\x1b[%sm %s \x1b[0m' % (format, "│")
            elif numberMatrix[j, i] == 4:
                format = ';'.join([str(1), str(32), str(40)])
                line += '\x1b[%sm %s \x1b[0m' % (format, "█")
            else:
                format = ';'.join([str(1), str(30), str(40)])
                line += '\x1b[%sm %s \x1b[0m' % (format, " ")

        num = round(yMax - priceJump*i, 2)
        numMax = round(yMax, 2)
        numStr = f'{num:.2f}'
        numMaxStr = f'{numMax:.2f}'

        if int(i) % 3 == 0:

            print("- " + numStr + " "*(len(numMaxStr) -
                  len(numStr)) + "  " + line + " ")
        else:
            print("  " + len(numMaxStr)*" " + "  " + line + " ")

    print("\n")
