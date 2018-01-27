import os


def config_directory(work_dir):
    if work_dir is not os.getcwd():
        os.chdir(work_dir)
    os.makedirs('tmp', exist_ok=True)


if __name__ == '__main__':
    config_directory(os.path.dirname(os.path.abspath(__file__)))

    from app import app

    app.run(port=8080)
