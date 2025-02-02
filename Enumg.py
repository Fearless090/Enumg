import dns.resolver
import argparse
from rich import print


parser = argparse.ArgumentParser(description='Subdomain Enumerator')
parser.add_argument('-d', '--domain', type=str, required=True, help='Base domain')
parser.add_argument('-w', '--wordlist', type=str, required=True, help='Path to subdomain wordlist')
parser.add_argument('-o', '--output', type=str, required=False, help='Path to output file')
parser.add_argument('-r', '--resolve', action='store_true', required=False, help='Resolve dns to ip address')
args = parser.parse_args()


def enumerate_subdomains(domain):
    subdomains = []
    
    # Perform a DNS query for common subdomains
    with open(args.wordlist) as file:
            common_subdomains = file.read().splitlines()
        
    for subdomain in common_subdomains:
        full_domain = f"{subdomain}.{domain}"
        
        try:
            answers = dns.resolver.resolve(full_domain, "A")
            
            for answer in answers:
                subdomains.append([full_domain,answer.address])
                
                if args.resolve is True:
                    print(f"Found subdomain: [blue]{full_domain}[/blue] - IP:[not bold]{answer.address}[/not bold]")
                else:
                    print(f"Found subdomain: [blue]{full_domain}[/blue]")

        except KeyboardInterrupt:
            exit("Exiting...")
        except:
            pass

    return subdomains


target_domain = args.domain
subdomains_found = enumerate_subdomains(target_domain)


print(f"Total subdomains found: {len(subdomains_found)}")

if args.output is not None:
    output_file = args.output
    with open(output_file, "w") as file:
        for subdomain in subdomains_found:
            file.write(f"{subdomain[0]} - {subdomain[1]} \n")
    print(f"Subdomains written to: {output_file}")
    
    
    
    
    
    
