import argparse
import src.data_processing.main as datapro
import src.orientation_visualizer.main as ornvisual


def main(args=None) -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--process', 
        action  = 'store_true', 
        help    = 'Running data_processing'
    )
    parser.add_argument(
        '--visual',
        action  = 'store_true',
        help    = 'Running orientation_visualizer'
    )
    arguments = parser.parse_args()
    process: callable = None 

    if arguments.process:
        print('[TEREKA App] Starting data_processing...')
        process = datapro.main

    elif arguments.visual:
        print('[TEREKA App] Starting orientation_visualizer...')
        process = ornvisual.main

    else:
        print('[TEREKA App] Unknown argument passed. Stopping program...')
        return

    process()


if __name__ == '__main__':
    main()