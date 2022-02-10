### cpu_generator.py
* The cpu_generator will generate a combination of the array `picking` based on the array `base_parameters`
    * example:
        ```
        base_parameters = [2, 16, 48, 'simple']
        picking = [8, 192, 256, 'complex']
        ```
        console printout:
        ```
        2_16_48_simple
        ...
        ...
        ...
        8_192_256_complex
        '2_16_48_simple': MyO3Processor(2, 16, 48, 'simple'),
        ...
        ...
        ...
        '8_192_256_complex': MyO3Processor(8, 192, 256, 'complex'),

        ```

### data_collector.py
* Collecting and generating csv file 
* path is the directories where the stats.txt is located. **Regular expression supported**.
* keyword is the string you want to match in stats.txt
    * example:
        ```
        # target file name is stats.txt
        filename = 'stats.txt'
        
        # search all the folders' name starting with 1644310610 under ./m5out
        path = './m5out/1644310610*/' 
        
        # search the line containing board.processor.cores.core.ipc
        keyword = 'board.processor.cores.core.ipc'
        ``` 
        console printout:
        ```
        {'2_16_256_simple': 
            {'RealMM': '1.172713', 'IntMM': '1.253004', 'Puzzle': '1.225295', 'Quicksort': '1.040971', 'Perm': '1.243710', 'Bubblesort': '1.335765', 'Towers': '1.186253', 'Treesort': '0.932959', 'Oscar': '1.275671', 'FloatMM': '1.175384', 'Queens': '1.073431'},
        ...
        ...
        ...
        '2_16_256_complex': 
            {'RealMM': '1.178562', 'Oscar': '1.276220', 'Puzzle': '1.223064', 'IntMM': '1.266648', 'Perm': '1.257213', 'Bubblesort': '1.346224', 'Towers': '1.170817', 'Treesort': '0.934710', 'Queens': '0.856763', 'Quicksort': '1.093794', 'FloatMM': '1.180530'}
        }
        ```
        file ouput:
        ```
        ggg.csv
        ```
        ![output file](https://i.imgur.com/YvGAd54.jpg)



