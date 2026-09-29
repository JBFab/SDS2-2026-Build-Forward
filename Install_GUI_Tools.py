##WRITTEN BY JASON BONDIOLI TO DETECT PYTHON LIBRARY VERSIONS IN USE IN THE
##SDS2 VERSION THIS SCRIPT IS EXECUTED FROM.  THIS WILL INSTALL COMPATIBLE VERSIONS
##OF POPULAR/NECESSARY LIBRARIES FOR RUNNING JB SPECIFIC TOOLS AND BUILDING
##FUTURE TOOLS. RUN THIS BEFORE USING JB CUSTOM MEMBERS OR PARAMETRICS TO ENSURE
##PROPER OPERATION.


import os
import sys
import ctypes
import subprocess

# ---------------------------------------------------------------------------
# Pre-defined Library List
# ---------------------------------------------------------------------------
LIBRARIES = [
    {
        "id": "1", 
        "name": "PySide/Qt", 
        "desc": "Advanced GUI Framework (Auto-matches your SDS2 version)", 
        "pip_name": "pyside",
        "selected": True, 
        "is_pyside": True
    },
    {
        "id": "2", 
        "name": "openpyxl", 
        "desc": "Read, write, and modify Excel (.xlsx) files natively", 
        "pip_name": "openpyxl",
        "selected": False, 
        "is_pyside": False
    },
    {
        "id": "3", 
        "name": "pandas", 
        "desc": "Powerful data analysis, manipulation, and CSV/Excel parsing", 
        "pip_name": "pandas",
        "selected": False, 
        "is_pyside": False
    },
    {
        "id": "4", 
        "name": "requests", 
        "desc": "Make HTTP web requests (download files, interact with APIs)", 
        "pip_name": "requests",
        "selected": False, 
        "is_pyside": False
    },
    {
        "id": "5", 
        "name": "pyodbc", 
        "desc": "Connect directly to SQL databases and external data sources", 
        "pip_name": "pyodbc",
        "selected": False, 
        "is_pyside": False
    },
    {
        "id": "6", 
        "name": "Pillow", 
        "desc": "The Python Imaging Library for opening, manipulating, and saving image files", 
        "pip_name": "pillow",
        "selected": False, 
        "is_pyside": False
    },
    {
        "id": "7", 
        "name": "PyMuPDF (fitz)", 
        "desc": "High-performance PDF rendering, parsing, and modification (imports as 'fitz')", 
        "pip_name": "pymupdf",
        "selected": False, 
        "is_pyside": False
    },
    {
        "id": "8", 
        "name": "ReportLab", 
        "desc": "The industry standard for generating complex, data-driven PDFs from scratch", 
        "pip_name": "reportlab",
        "selected": False, 
        "is_pyside": False
    },
    {
        "id": "9", 
        "name": "Trimesh", 
        "desc": "Pure Python library for loading, analysis, and visualization of 3D meshes", 
        "pip_name": "trimesh",
        "selected": False, 
        "is_pyside": False
    },
    {
        "id": "10", 
        "name": "PyVista", 
        "desc": "Advanced 3D plotting, visualization, and mesh analysis", 
        "pip_name": "pyvista",
        "selected": False, 
        "is_pyside": False
    }
]

# ---------------------------------------------------------------------------
# Initialization & Administrator Check
# ---------------------------------------------------------------------------
bin_dir = os.path.dirname(sys.executable)
python_exe = os.path.join(bin_dir, "python.exe")

if not os.path.exists(python_exe):
    python_exe = sys.executable

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    print("Requesting Administrator privileges...")
    ctypes.windll.shell32.ShellExecuteW(None, "runas", python_exe, f'"{os.path.abspath(__file__)}"', None, 1)
    sys.exit()

# ---------------------------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------------------------
def get_qt_version(b_dir):
    for dll in ['Qt6Core.dll', 'Qt5Core.dll']:
        dll_path = os.path.join(b_dir, dll)
        if os.path.exists(dll_path):
            cmd = f'(Get-Item "{dll_path}").VersionInfo.FileVersion'
            result = subprocess.run(["powershell", "-NoProfile", "-Command", cmd], capture_output=True, text=True)
            if result.returncode == 0 and result.stdout.strip():
                version = result.stdout.strip()
                parts = version.split('.')
                if len(parts) >= 2:
                    return parts[0], parts[1], dll
    return None, None, None

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_menu():
    clear_screen()
    print("==================================================")
    print("  SDS2 Python Environment & Library Installer")
    print("==================================================")
    print(f"\nDetected SDS2 bin path: {bin_dir}\n")
    print("Select the libraries you want to install for this SDS2 version:\n")
    
    for lib in LIBRARIES:
        box = "[X]" if lib["selected"] else "[ ]"
        # Spacing logic to keep columns aligned for double-digit IDs
        spacer = " " if len(lib["id"]) < 2 else ""
        print(f"  {box} {lib['id']}.{spacer} {lib['name']}")
        print(f"         - {lib['desc']}")
        print("")
        
    print("--------------------------------------------------")
    print(" Commands: [Number] Toggle | [A] Select All | [C] Clear ")
    print("           [I] Install Selected | [Q] Quit")
    print("--------------------------------------------------")

# ---------------------------------------------------------------------------
# Main Interactive Loop
# ---------------------------------------------------------------------------
while True:
    draw_menu()
    choice = input("\nEnter command: ").strip().upper()
    
    if choice == 'Q':
        sys.exit()
    elif choice == 'A':
        for lib in LIBRARIES: lib["selected"] = True
    elif choice == 'C':
        for lib in LIBRARIES: lib["selected"] = False
    elif choice == 'I':
        break 
    else:
        # Toggle specific numbers
        for lib in LIBRARIES:
            if choice == lib["id"]:
                lib["selected"] = not lib["selected"]

# ---------------------------------------------------------------------------
# Installation Sequence
# ---------------------------------------------------------------------------
selected_libs = [lib for lib in LIBRARIES if lib["selected"]]

if not selected_libs:
    print("\nNo libraries selected. Exiting...")
    input("Press Enter to close...")
    sys.exit()

clear_screen()
print("==================================================")
print("  INSTALLING LIBRARIES...")
print("==================================================")

# 1. Unlock the Embedded Environment
print("\n[Step 1] Checking environment lock...")
pth_files = [f for f in os.listdir(bin_dir) if f.startswith('python') and f.endswith('._pth')]
if not pth_files:
    print("         No ._pth file found. Skipping unlock.")
else:
    for pth in pth_files:
        pth_path = os.path.join(bin_dir, pth)
        with open(pth_path, "r") as f:
            content = f.read()
        
        modified = False
        if "#import site" in content:
            content = content.replace("#import site", "import site")
            modified = True
        elif "# import site" in content:
            content = content.replace("# import site", "import site")
            modified = True
        elif "import site" not in content:
            content += "\nimport site\n"
            modified = True
            
        if modified:
            with open(pth_path, "w") as f:
                f.write(content)
            print(f"         Unlocked embedded environment in {pth}")
        else:
            print(f"         Environment already unlocked in {pth}")

# 2. Install Packages
print("\n[Step 2] Fetching and installing packages...")

for lib in selected_libs:
    print(f"\n---> Installing {lib['name']}...")
    
    if lib["is_pyside"]:
        major, minor, dll_name = get_qt_version(bin_dir)
        if not major:
            print("     [ERROR] Could not detect Qt Core DLLs. Skipping PySide.")
            continue
            
        print(f"     Detected {dll_name} version: {major}.{minor}.x")
        
        if major == '6':
            target_package = f"PySide6~={major}.{minor}.0"
            uninstalls = ["PySide6", "PySide6-Addons", "PySide6-Essentials", "shiboken6"]
        else:
            target_package = f"PySide2~={major}.{minor}.0"
            uninstalls = ["PySide2", "shiboken"]

        print("     Cleaning up any mismatched versions...")
        subprocess.run([python_exe, "-m", "pip", "uninstall", "-y"] + uninstalls, capture_output=True)

        print(f"     Installing exact ABI match ({target_package})...")
        subprocess.run([python_exe, "-m", "pip", "install", target_package])
    
    else:
        subprocess.run([python_exe, "-m", "pip", "install", lib["pip_name"]])

print("\n==================================================")
print("  INSTALLATION COMPLETE!")
print("  Please fully restart SDS2 to apply any changes.")
print("==================================================")
input("Press Enter to close this window...")
