import os
import shutil

folders_to_clean = [
    '/Users/macbook/Desktop',
    '/Users/macbook/Downloads'
]
files_categories = {
    'images':['.jpeg', '.jpg', '.tiff', '.gif', '.bmp', '.png', '.bpg', 'svg', '.heif', '.psd', 'avif', 'webp'],
    'videos':['.avi', '.flv', '.wmv', '.mov', '.mp4', '.webm', '.vob', '.mng', '.qt', '.mpg', '.mpeg', '.3gp'],
    'audios':['.aa', '.aac', '.aax', '.act', '.aiff', '.alac', '.amr', '.ape', '.au', '.awb', '.dct', '.dss', '.dvf', '.flac', '.gsm', '.iklax', '.ivs', '.m4a', '.m4b', '.m4p', '.mmf', '.mp3', '.mpc', '.msv', '.nmf', '.nsf', '.ogg', '.oga', '.mogg', '.opus', '.ra', '.rm', '.raw', '.rf64', '.sln', '.tta', '.voc', '.vox', '.wav', '.wma', '.wv', '.8svx'],
    'documents':['.oxps', '.epub', '.pages', '.docx', '.doc', '.fdf', '.ods', '.odt', '.pwi', '.xsn', '.xps', '.dotx', '.docm', '.dox', '.rvg', '.rtf', '.rtfd', '.wpd', '.xls', '.xlsx', '.ppt', '.pptx', '.csv', '.pdf', '.odp', '.pps', '.ppsx', '.odt', '.txt', '.in', '.out', '.md'],
    'archives':['.a', '.ar', '.cpio', '.iso', '.tar', '.gz', '.rz', '.7z', '.dmg', '.rar', '.xar', '.zip'],
    'disk_images':['.bin', '.dmg', '.toast', '.vcd'],
    'programming_files':['.py', '.c', '.cpp', '.h', '.java', '.class', '.cs', 'html', '.css', '.js', '.php', '.xhtml', '.sql', 'json'],
    'executables':['.exe', '.apk', '.bat', '.bin', '.cgi', '.pl', '.com', '.gadget', '.jar', '.msi', '.py', '.wsf'],
    'fonts':['.fnt', '.fon', '.otf', '.ttf', '.woff'],
    'presentations':['.key', '.odp', '.pps', '.ppt', '.pptx'],
    'spreadsheets':['.ods', '.xls', '.xlsm', '.xlsx'],

}

def organize_folders(folder_path, file_extensions):
    files = os.listdir(folder_path)
    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):  # Ensure it's a file
            for category, extensions in file_extensions.items():
                if any(file.lower().endswith(ext) for ext in extensions):
                    category_path = os.path.join(folder_path, category)
                    if not os.path.exists(category_path):
                        os.makedirs(category_path)
                    target_path = os.path.join(category_path, file)
                    try:
                        shutil.move(file_path, target_path)
                    except FileNotFoundError as e:
                        print(f"File not found: {file_path} -> {e}")
                    except PermissionError as e:
                        print(f"Permission denied: {file_path} -> {e}")
                    except Exception as e:
                        print(f"Error moving {file_path} to {target_path}: {e}")
                    break  # Stop checking other categories after the first match

for folder in folders_to_clean:
    organize_folders(folder, files_categories)

print("Done organizing files!")