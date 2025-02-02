

# Enumg

Enumg is a simple Python-based subdomain enumeration tool that helps identify subdomains associated with a given domain using DNS queries.

## Features

- Resolves IP addresses of discovered subdomains with ```--reslove``` flag.
- Identify if a subdomain has more than one IP address.
- Outputs results to a text file.

## Usage

1. Clone or download this script to your local machine.
2. Run the script by providing a target domain:

```python
python Enumg.py [-h] -d DOMAIN -w WORDLIST [-o OUTPUT] [-r/--reslove]
```

3. The discovered subdomains will be printed in the terminal and saved to a text file.

## Example

```bash
└─$ Enumg.py -d example.com -w common.txt --resolve -o subdomains.txt
Found subdomain: www.example.com - IP: 93.184.216.34
Found subdomain: blog.example.com - IP: 93.184.216.35
Total subdomains found: 2
Subdomains written to: subdomains.txt
```

## Legal Disclaimer

This tool is intended for educational and authorized testing purposes only. Do not use it on domains without explicit permission.

