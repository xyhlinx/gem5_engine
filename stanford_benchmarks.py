
from gem5.resources.resource import CustomResource

Bubblesort = CustomResource('Stanford/Bubblesort')
IntMM = CustomResource('Stanford/IntMM')
Perm = CustomResource('Stanford/Perm')
Queens = CustomResource('Stanford/Queens')
RealMM = CustomResource('Stanford/RealMM')
Treesort = CustomResource('Stanford/Treesort')
FloatMM = CustomResource('Stanford/FloatMM')
Oscar = CustomResource('Stanford/Oscar')
Puzzle = CustomResource('Stanford/Puzzle')
Quicksort = CustomResource('Stanford/Quicksort')
Towers = CustomResource('Stanford/Towers')

benchmarks = {
    "Bubblesort": Bubblesort,
    "IntMM": IntMM,
    "Perm": Perm,
    "Queens": Queens,
    "RealMM": RealMM,
    "Treesort": Treesort,
    "FloatMM": FloatMM,
    "Oscar": Oscar,
    "Puzzle": Puzzle,
    "Quicksort": Quicksort,
    "Towers": Towers,
}
