import re

def extract_ips(file_path):
    # Expression régulière pour extraire les adresses IP
    ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

    # Extraction des adresses IP sans protocole
    with open(file_path, "r") as file:
        ips_with_protocol = file.readlines()
    ips_without_protocol = [re.search(ip_pattern, ip).group() for ip in ips_with_protocol]

    return ips_without_protocol

def save_ips(file_path, ips):
    # Enregistrement des adresses IP sans protocole dans un nouveau fichier
    output_file_path = file_path.split(".")[0] + "_nude.txt"
    with open(output_file_path, "w") as output_file:
        for ip in ips:
            output_file.write(ip + "\n")

def main():
    file_path = input("fichier_ips.txt")
    ips = extract_ips(file_path)
    save_ips(file_path, ips)

if __name__ == "__main__":
    main()