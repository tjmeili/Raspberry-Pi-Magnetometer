import os.path
import google_drive_handler as drive

def main():
    drive.initialize()
    drive.upload_file("file2.txt")


if __name__ == '__main__':
    main()