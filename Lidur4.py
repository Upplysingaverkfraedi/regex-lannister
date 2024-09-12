import requests
import pandas as pd
import argparse
import re

def parse_arguments():
    parser = argparse.ArgumentParser(description='Vinna með úrslit af tímataka.net.')
    parser.add_argument('--url', help='Slóð að vefsíðu með úrslitum.')
    parser.add_argument('--output', required=True, help='Slóð að útgangsskrá til að vista niðurstöðurnar (CSV format).')
    parser.add_argument('--debug', action='store_true', help='Vistar html í skrá til að skoða.')
    return parser.parse_args()

def fetch_html(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Tókst ekki að sækja gögn af {url}")
        return None

def parse_html(html):
    # Regluleg segð til að finna allar <tr> töflur
    row_pattern = re.compile(r'<tr>(.*?)</tr>', re.DOTALL)
    # Regluleg segð til að finna <td> innan hverrar <tr> töflu
    column_pattern = re.compile(r'<td[^>]*>(.*?)</td>', re.DOTALL)

    rows = row_pattern.findall(html)
   
    # Sækir gögn frá öllum línum 
    data = []
    for row in rows:
        columns = column_pattern.findall(row)
        columns = [re.sub(r'<[^>]+>', '', column).strip() for column in columns]
        if columns:  
            data.append(columns)
    
    return data

def skrifa_nidurstodur(data, output_file):
    if not data:
        print("Engar niðurstöður til að skrifa.")
        return

    df = pd.DataFrame(data)
    df.to_csv(output_file, sep=',', index=False, header=False)
    print(f"Niðurstöður vistaðar í '{output_file}'.")

def main():
    args = parse_arguments()

    # Athuga hvort URL sé frá timataka.net og hafi 'urslit'
    if not ('timataka.net' in args.url and 'urslit' in args.url):
        print("Slóðin er ekki frá timataka.net eða ekki með úrslitum.")
        return

    html = fetch_html(args.url)
    if not html:
        raise Exception("Ekki tókst að sækja HTML gögn, athugið URL.")

    if args.debug:
        html_file = args.output.replace('.csv', '.html')
        with open(html_file, 'w') as file:
            file.write(html)
        print(f"HTML fyrir {args.url} vistað í {html_file}")

    results = parse_html(html)
    skrifa_nidurstodur(results, args.output)

if __name__ == "__main__":
    main()

