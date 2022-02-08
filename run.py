

from riscv_se import MyO3Processor, RiscvSEBoard
from gem5.simulate.simulator import Simulator
from stanford_benchmarks import *


def run_experiment(core_type, workload):
    board = RiscvSEBoard(core_type)

    board.set_se_binary_workload(workload)

    simulator = Simulator(board=board, full_system=False)

    simulator.run()

cores = {
    '8_16_48_simple': MyO3Processor(8, 16, 48, 'simple'),
    '2_192_48_simple': MyO3Processor(2, 192, 48, 'simple'),
    '2_16_256_simple': MyO3Processor(2, 16, 256, 'simple'),
    '2_16_48_complex': MyO3Processor(2, 16, 48, 'complex'),
    '8_192_48_simple': MyO3Processor(8, 192, 48, 'simple'),
    '8_16_256_simple': MyO3Processor(8, 16, 256, 'simple'),
    '8_16_48_complex': MyO3Processor(8, 16, 48, 'complex'),
    '2_192_256_simple': MyO3Processor(2, 192, 256, 'simple'),
    '2_192_48_complex': MyO3Processor(2, 192, 48, 'complex'),
    '2_16_256_complex': MyO3Processor(2, 16, 256, 'complex'),
    '8_192_256_simple': MyO3Processor(8, 192, 256, 'simple'),
    '8_192_48_complex': MyO3Processor(8, 192, 48, 'complex'),
    '8_16_256_complex': MyO3Processor(8, 16, 256, 'complex'),
    '2_192_256_complex': MyO3Processor(2, 192, 256, 'complex'),
    '8_192_256_complex': MyO3Processor(8, 192, 256, 'complex'),

    "LargeCore": MyO3Processor(8, 16, 48, 'simple'),
    "SmallCore": MyO3Processor(2, 16, 48, 'simple'),
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
