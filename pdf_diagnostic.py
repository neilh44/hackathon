import sys
import pkg_resources

def check_pdf_setup():
    """
    Diagnostic function to check PDF processing setup
    """
    results = {
        "python_version": sys.version,
        "packages": {},
        "fitz_import": None,
        "fitz_version": None
    }
    
    # Check installed packages
    required_packages = ['PyMuPDF', 'Pillow', 'pytesseract']
    for package in required_packages:
        try:
            version = pkg_resources.get_distribution(package).version
            results["packages"][package] = {
                "installed": True,
                "version": version
            }
        except pkg_resources.DistributionNotFound:
            results["packages"][package] = {
                "installed": False,
                "version": None
            }
    
    # Try different import methods
    try:
        from PyMuPDF import fitz
        results["fitz_import"] = "Success: from PyMuPDF import fitz"
        results["fitz_version"] = fitz.version
    except ImportError:
        try:
            import fitz
            results["fitz_import"] = "Success: import fitz"
            results["fitz_version"] = fitz.version
        except ImportError:
            results["fitz_import"] = "Failed: Both import methods failed"
    except Exception as e:
        results["fitz_import"] = f"Error: {str(e)}"
    
    return results

def print_diagnostic_results(results):
    """
    Print diagnostic results in a readable format
    """
    print("\n=== PDF Processing Setup Diagnostic Results ===")
    print(f"\nPython Version: {results['python_version']}")
    
    print("\nRequired Packages:")
    for package, info in results["packages"].items():
        status = "✓" if info["installed"] else "✗"
        version = info["version"] if info["installed"] else "Not installed"
        print(f"{status} {package}: {version}")
    
    print(f"\nFitz Import Status: {results['fitz_import']}")
    print(f"Fitz Version: {results['fitz_version']}")

if __name__ == "__main__":
    results = check_pdf_setup()
    print_diagnostic_results(results)