

from riscv_se import MyO3Processor, RiscvSEBoard
from gem5.simulate.simulator import Simulator
from stanford_benchmarks import *


def run_experiment(core_type, workload):
    board = RiscvSEBoard(core_type)

    board.set_se_binary_workload(workload)

    simulator = Simulator(board=board, full_system=False)

    simulator.run()

    """
    "c8_192_256"
    "s8_192_256"
    "c_8_192_48"
    "s_8_192_48"
    "c_2_192_256"
    "s_2_192_256
    """
cores = {
    "c_8_192_256": MyO3Processor(8, 192, 256, 'complex'),
    "s_8_192_256": MyO3Processor(8, 192, 256, 'simple'),
    "c_8_192_48": MyO3Processor(8, 192, 48, 'complex'),
    "s_8_192_48": MyO3Processor(8, 192, 48, 'simple'),
    "c_2_192_256": MyO3Processor(2, 192, 256, 'complex'),
    "s_2_192_256": MyO3Processor(2, 192, 256, 'simple'),
    "c_8_16_256": MyO3Processor(8, 16, 256, 'complex'),
    "s_8_16_256": MyO3Processor(8, 16, 256, 'simple'),
    # "LargeCore": MyO3Processor(8, 192, 256, 'complex'),
    # "LargeCore": MyO3Processor(2, 16, 256, 'simple'),
    # "LargeCore": MyO3Processor(2, 192, 48, 'simple'),
    # "LargeCore": MyO3Processor(8, 16, 48, 'simple'),
    # "SmallCore": MyO3Processor(2, 16, 48, 'simple'),
}

if __name__ == "__m5_main__":

    from argparse import ArgumentParser
    parser = ArgumentParser(
        description="A script to run RISC-V O3 cores and the stanford benchmarks"
    )

    parser.add_argument("benchmark", choices=benchmarks.keys())
    parser.add_argument("core_type", choices=cores.keys())

    args = parser.parse_args()

    run_experiment(cores[args.core_type], benchmarks[args.benchmark])
