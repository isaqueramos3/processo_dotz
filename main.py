from utils.utils import yamlConfig, download_files, restore_downloads
from src.bills import Bills
from src.comp import Comp
from src.price import Price

# functions

try:
    fp = yamlConfig()
    print("Yaml config file readed")
except:
    print("Yaml config file could not be readed")

raw_bucket = fp["gcp_paths"]["raw"]["bucket"]

# download files to remote path
download_files(raw_bucket)

# call functions files
try:
    Bills()
    print("Bills dataset loaded in Mysql")
except:
    print("Bills dataset could not be loaded")
try:
    Comp()
    print("Comp dataset loaded in Mysql")
except:
    print("Comp dataset could not be loaded in Mysql")
try:
    Price()
    print("Price dataset load in Mysql")
except:
    print("Price dataset could not be loaded in Mysql")

# restore downloads file
restore_downloads()