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
        '--visualRaw',
        action  = 'store_true',
        help    = 'Running orientation_visualizer'
    )
    parser.add_argument(
        '--visualFilter',
        action  = 'store_true',
        help    = 'Running orientation_visualizer'
    )
    arguments = parser.parse_args()
    process: callable = None 

    if arguments.process:
        print('[TEREKA_app] Starting data_processing...')
        process = datapro.main

    elif arguments.visualRaw:
        print('[TEREKA_app] Starting orientation_visualizer (raw)...')
        process = ornvisual.main(False)

    elif arguments.visualFilter:
        print('[TEREKA_app] Starting orientation_visualizer (filter)...')
        process = ornvisual.main(True)

    else:
        print('[TEREKA_app] Unknown argument passed. Stopping program...')
        return

    process()
    print('[TEREKA_app] Stopped!')


if __name__ == '__main__':
    main()