from libs.pylib.buffer_io.standard_input_buffer import StandardInputBuffer
from src.mediators.stream_mediator import StreamMediator


def main():
    StreamMediator \
        .set_buffer(StandardInputBuffer()) \
        .read_config() \
        .stream()


if __name__ == "__main__":
    main()
