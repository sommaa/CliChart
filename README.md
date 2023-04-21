<a name="readme-top"></a>
<div align="center">

![](https://img.shields.io/badge/python-%232C2D72.svg?style=for-the-badge&logo=python&logoColor=white)
![](https://img.shields.io/github/last-commit/sommaa/CliChart?&style=for-the-badge&color=CFFC49&logoColor=171718&labelColor=171718)
![](https://img.shields.io/github/stars/sommaa/CliChart?style=for-the-badge&logo=starship&color=8bd5ca&logoColor=D9E0EE&labelColor=171718)
[![](https://img.shields.io/github/repo-size/sommaa/CliChart?color=%23DDB6F2&label=SIZE&logo=codesandbox&style=for-the-badge&logoColor=D9E0EE&labelColor=171718)](https://github.com/sommaa/Clichart)

</div >

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/sommaa/CliChart">
    <img src="https://user-images.githubusercontent.com/120776791/233722279-7a1e8baf-5292-4f01-a411-185fde5782d0.png" alt="Logo" width="154" height="160">
    <br />
    <br />
  </a>
  <a href="https://github.com/sommaa/CliChart">
    <img src="https://user-images.githubusercontent.com/120776791/233723970-f3269bcd-6c67-4a74-a397-d368a025f575.png" alt="Logo" width="300" height="55">
  </a>

  <h3 align="center">A terminal based python script to display crypto price trends</h3>
  <p align="center">
    <a href="https://github.com/sommaa/CliChart/issues">Report Bug</a>
    ·
    <a href="https://github.com/sommaa/CliChart/issues">Request Feature</a>
  </p>
</div>

<div align="center">

<a href='https://ko-fi.com/sommaa' target='_blank'><img height='35' style='border:0px;height:46px;' src='https://az743702.vo.msecnd.net/cdn/kofi3.png?v=0' border='0' alt='Buy Me a Coffee at ko-fi.com' />

</div>

<br />

# :money_mouth_face: Showcase

![2023-04-21_22-00](https://user-images.githubusercontent.com/120776791/233724896-058b3485-4d35-4274-8fee-4f82a169c784.png)

# :stars: Features

- Price data directly from [CoinGecko APIs](https://www.coingecko.com/en/api/documentation)
- Easily resizable
- Customizable timeframe
- Adapts to your shell theme
- Actual price

# :notebook: Documentation

### Options:
```
  -h, --help            show this help message and exit
  -c COIN, --coin COIN  coin to display (example: bitcoin)
  -b BASE, --base BASE  base currency (example: usd)
  -d DAYS, --days DAYS  days ago (inputs: 1/7/14/30/90/180/365)
  -x HLIM, --hlim HLIM  height of the terminal box
  -y VLIM, --vlim VLIM  width of the terminal box
```
### Example:

```bash
./CliChart -d 14 -c "bitcoin" -b "usd" -y 25 -x 40
```

### Installation:

- Clone CliChart repository:
```bash
  git clone https://github.com/sommaa/CliChart.git
```

- Add this line to your .bashrc or .zshrc file to export the path:
```bash
  export PATH=$PATH:/where/you/saved/the/file/CliChart
```
