<a id="readme-top"></a>

<!-- PROJECT LOGO -->
<br />

<h3 align="center">Ethereum Price Alert Bot 🚨</h3>

  <p align="center">
    Monitors Ethereum price fluctuations and sends desktop notifications for significant crashes 📉 or spikes 🚀
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Back in 2020, I mined some Ethereum and pretty much forgot about it. Turns out my MetaMask wallet’s been sitting on a decent gain—but I haven’t been keeping up with the market. I decided this was the perfect opportunity to sharpen my Python skills and get some hands-on experience with automation. That’s what spawned this project: a bot that watches the price for me. If Ethereum tanks or takes off, I get a desktop pop-up notification so I can decide whether to cash in or bail before it’s too late.

In the future, I might expand it to track multiple coins (if I buy them) or send alerts to my phone via text or email.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

[![OS: Linux][Linux-badge]][Linux-url]
[![Python][Python-badge]][Python-url]
[![Status][Status-badge]][Status-url]
[![License][License-badge]][License-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these steps! 📝

### Prerequisites
* Python 3.12+
* pip

### Installation
 
1. Clone the repo
   
   ```sh
    git clone https://github.com/your_username/ethereum-price-signal-bot.git
   
    cd ethereum-price-signal-bot

   ```
3. Install dependencies
   
   ```sh
    pip install -r requirements.txt

    ```
4. Run the script

    ```sh
    python3 main.py
    ```
    
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Once the script is running, it fetches the Ethereum price every 10 minutes. If the price has dropped significantly in the past 24 hours, a desktop notification will appear with the signal 


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Nicholas Colon - www.linkedin.com/in/nick-colon - nickcolon1340@gmail.com

Project Link: [https://github.com/nicholas-net/crypto-price-signal-bot](https://github.com/nicholas-net/crypto-price-signal-bot)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Python-badge]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org
[Linux-badge]: https://img.shields.io/badge/OS-Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black
[Linux-url]: https://www.linux.org/
[Status-badge]: https://img.shields.io/badge/status-active-brightgreen?style=for-the-badge
[Status-url]: #

[License-badge]: https://img.shields.io/badge/license-MIT-green?style=for-the-badge
[License-url]: https://opensource.org/licenses/MIT




