from hda import Client
import os 

hda_client = Client()

query = {
  "dataset_id": "EO:ESA:DAT:SENTINEL-2",
  "bbox": [
    36.682493120000004,
    -1.14858368,
    37.42603097,
    -0.54936891
  ],
  "productType": "S2MSI1C",
  "processingLevel": "S2MSI1C",
  "instrument": "MSI",
  "startdate": "2024-12-01T00:00:00.000Z",
  "enddate": "2024-12-31T23:59:59.999Z",
  "itemsPerPage": 200,
  "startIndex": 0
}
matches = hda_client.search(query)
print(f"Found {len(matches)} matching products. ")


# Specify a custom directory for downloads
output_path = "/path/to/custom_directory"
os.makedirs(output_path, exist_ok=True)  # Create the directory if it doesn't exist

# Download all matching products to the specified directory
matches.download(output_path)
print(f"Downloaded products to: {output_path}")






