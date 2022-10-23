# Bitly API service

**Bitly API service** interacts with [Bitly](https://bitly.com/pages/home/v1) and helps you in work with links. It can shorten income links creating bitlink or check your bitlink and return number of views.

## Getting Started

Below you will find instructions on how to use **Bitly API service**.  

### Prerequisites

Please be sure that **Python3** is already installed. 

### Installing
1. Clone the repository:
```
git clone https://github.com/MiraNizam/Bitly-API-service.git
```
2. Now you need to receive your own unique **GENERIC ACCESS TOKEN** to do this, you need to log in to the site and [generate token](https://app.bitly.com/settings/api/).

3. Create **.env** file with unique environmental variable, that was created above. 

| API_TOKEN=unique value  | 
|----------------------------------|

4. Use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
5. How to run code:

Input: 
```
main.py https://www.google.com/
```
Output example: 
`Your bitlink: bit.ly/3gt5PHb`

Input:
```
main.py bit.ly/3gt5PHb
```
Output example:
`
Bitlink clicks: 3
`