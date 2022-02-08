

from gem5.components.boards.simple_board import SimpleBoard
from gem5.components.cachehierarchies.classic.\
    private_l1_private_l2_cache_hierarchy import (
        PrivateL1PrivateL2CacheHierarchy,
    )
from gem5.components.memory import SingleChannelDDR3_1600
from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.components.processors.cpu_types import CPUTypes

from m5.objects.BranchPredictor import *

branch_predictors = {
    'simple':  TournamentBP,
    'ltage': TAGE_SC_L_TAGE_64KB,
    'perceptron': MultiperspectivePerceptron64KB,
    'complex': MultiperspectivePerceptronTAGE64KB,
}

class MyO3Processor(SimpleProcessor):
    def __init__(self, width, rob_size, num_regs, branch_predictor):
        """A simple to configure single core out-of-order processor.

        :param width: The pipeline width. Max value is 8.
        :param rob_size: The number of entries in the reorder buffer
        :param num_regs: The number of physical register for both integer and
            floating point register files.
        :param branch_predictor: One of the options in `branch_predictors`
        """
        super().__init__(cpu_type = CPUTypes.O3, num_cores=1)

        self.cores[0].core.fetchWidth = width
        self.cores[0].core.decodeWidth = width
        self.cores[0].core.renameWidth = width
        self.cores[0].core.issueWidth = width
        self.cores[0].core.wbWidth = width
        self.cores[0].core.commitWidth = width

        self.cores[0].core.numROBEntries = rob_size

        self.cores[0].core.numPhysIntRegs = num_regs
        self.cores[0].core.numPhysFloatRegs = num_regs

        self.cores[0].core.branchPred = branch_predictors[branch_predictor]()

class RiscvSEBoard(SimpleBoard):

    def __init__(self, processor):
        """A simple RISC-V SE mode board.

        Has a small (512 MiB) DDR3 memory. This is small to support faster
        execution.
        Has a 2-level hierarchy.
        Can use any processor, but it is designed to be used with the simple
        O3 processor `MyO3Processor`.
        Runs at 2GHz.
        """

        memory = SingleChannelDDR3_1600(size="512MiB")
        cache_hierarchy = PrivateL1PrivateL2CacheHierarchy(
            l1d_size="32KiB", l1i_size="32KiB", l2_size="512KiB"
        )

        super().__init__(
            clk_freq="2GHz",
            processor=processor,
            memory=memory,
            cache_hierarchy=cache_hierarchy,
        )
