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

    if arguments.process:
        print('[TEREKA_app] Starting data_processing...')
        datapro.main()

    elif arguments.visual:
        print('[TEREKA_app] Starting orientation_visualizer...')
        ornvisual.main()

    else:
        print('[TEREKA_app] Unknown argument passed. Stopping program...')
        return


if __name__ == '__main__':
    main()