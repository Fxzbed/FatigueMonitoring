from face_detect import FaceDetect
from shell_config_parse import ShellConfigParser

def main():
    face_detector = None
    args = ShellConfigParser().get_args()
    try:
        face_detector = FaceDetect(args)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    main()
