import tkinter as tk
import random
import time
import math

class SortVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Visualizer")
        self.root.geometry("1000x1000")
        self.canvas = tk.Canvas(self.root, width=800, height=400, bg="black")
        self.canvas.pack()

        # Default array size
        self.arr_size = 100
        self.arr = list(range(1, self.arr_size + 1))
        self.shuffle_array()

        # Algorithm Information Label
        self.algorithm_label = tk.Label(self.root, text="Algorithm: None", font=("Arial", 14), bg="black", fg="white")
        self.algorithm_label.pack(pady=10)

        # Algorithm Description Label
        self.description_label = tk.Label(self.root, text="Description: None", font=("Arial", 10), bg="black", fg="white", wraplength=800)
        self.description_label.pack(pady=10)

        # Sorting Time Label
        self.time_label = tk.Label(self.root, text="Sorting Time: 0.0s", font=("Arial", 12), bg="black", fg="white")
        self.time_label.pack(pady=10)

        # Buttons to choose sorting algorithm
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        buttons = [
            ("Odd-Even Sort", "Odd-Even Sort", "A sorting algorithm that works by alternately sorting odd and even indexed elements.", self.start_odd_even_sort),
            ("Merge Sort", "Merge Sort", "A divide-and-conquer algorithm that splits the array into halves, sorts them and merges them back together.", self.start_merge_sort),
            ("Tim Sort", "Tim Sort", "A hybrid sorting algorithm derived from merge sort and insertion sort, optimized for real-world data.", self.start_tim_sort),
            ("Quick Sort", "Quick Sort", "A divide-and-conquer algorithm that selects a pivot element and partitions the array around the pivot.", self.start_quick_sort),
            ("Selection Sort", "Selection Sort", "A simple algorithm that repeatedly selects the smallest element and places it at the beginning of the array.", self.start_selection_sort),
            ("LSD Radix Sort", "LSD Radix Sort", "A non-comparative integer sorting algorithm that sorts data by processing individual digits.", self.start_lsd_radix_sort),
            ("Bubble Sort", "Bubble Sort", "A simple comparison-based algorithm that repeatedly swaps adjacent elements if they are in the wrong order.", self.start_bubble_sort),
            ("Cocktail Shaker Sort", "Cocktail Shaker Sort", "A bidirectional version of bubble sort that moves through the array in both directions.", self.start_cocktail_sort),
            ("BogoSort", "BogoSort", "A highly ineffective sorting algorithm that randomly shuffles the array until it is sorted.", self.start_bogo_sort),
            ("Grail Sort", "Grail Sort", "A merge-based sorting algorithm that merges two sorted blocks in place.", self.start_grail_sort)
        ]

        for col, (text, algorithm_name, description, command) in enumerate(buttons):
            button = tk.Button(frame, text=text, command=lambda name=algorithm_name, desc=description, cmd=command: self.update_algorithm_info(name, desc, cmd))
            button.grid(row=0, column=col, padx=5)

        # Add a Reset Button
        self.reset_button = tk.Button(self.root, text="Reset", command=self.reset, font=("Arial", 12), bg="red", fg="white")
        self.reset_button.pack(pady=20)

    def reset(self):
        """Reset the array to its initial state and redraw the bars"""
        self.arr_size = 100
        self.arr = list(range(1, self.arr_size + 1))  # Recreate the array
        self.shuffle_array()  # Shuffle the array
        self.draw_bars()  # Redraw the bars on the canvas
        self.algorithm_label.config(text="Algorithm: None")  # Reset algorithm name
        self.description_label.config(text="Description: None")  # Reset description
        self.time_label.config(text="Sorting Time: 0.0s")  # Reset time label

    def update_algorithm_info(self, algorithm_name, description, command):
        """Update algorithm info and description label, then execute the sorting algorithm"""
        self.algorithm_label.config(text=f"Algorithm: {algorithm_name}")
        self.description_label.config(text=f"Description: {description}")
        command()  # Execute the algorithm's corresponding function

    def shuffle_array(self):
        """Shuffle the array and redraw the bars"""
        random.shuffle(self.arr)
        self.draw_bars()

    def draw_bars(self, highlight_indices=None):
        """Draw the array as bars on the canvas"""
        self.canvas.delete("all")
        width = 800 / len(self.arr)  # Dynamic width based on array size
        for i, height in enumerate(self.arr):
            color = "white" if highlight_indices is None or i not in highlight_indices else "red"
            x0 = i * width
            y0 = 400 - height * 4  # Scale height to fit in canvas
            x1 = (i + 1) * width
            y1 = 400
            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline=color)
        self.root.update()

    def display_sorting_time(self, time_taken):
        """Display the time taken for sorting"""
        self.time_label.config(text=f"Sorting Time: {time_taken:.4f}s")

    def start_odd_even_sort(self):
        self.shuffle_array()
        start_time = time.time()
        self.odd_even_sort()
        end_time = time.time()
        self.display_sorting_time(end_time - start_time)

    def start_merge_sort(self):
        self.shuffle_array()
        start_time = time.time()
        self.merge_sort(0, len(self.arr) - 1)
        end_time = time.time()
        self.display_sorting_time(end_time - start_time)

    def start_tim_sort(self):
        self.shuffle_array()
        start_time = time.time()
        self.tim_sort()
        end_time = time.time()
        self.display_sorting_time(end_time - start_time)

    def start_quick_sort(self):
        self.shuffle_array()
        start_time = time.time()
        self.quick_sort(0, len(self.arr) - 1)
        end_time = time.time()
        self.display_sorting_time(end_time - start_time)
    
    def start_selection_sort(self):
        self.shuffle_array()
        start_time = time.time()
        self.selection_sort()
        end_time = time.time()
        self.display_sorting_time(end_time - start_time)

    def start_lsd_radix_sort(self):
        self.shuffle_array()
        start_time = time.time()
        self.lsd_radix_sort()
        end_time = time.time()
        self.display_sorting_time(end_time - start_time)

    def start_bubble_sort(self):
        self.shuffle_array()
        start_time = time.time()
        self.bubble_sort()
        end_time = time.time()
        self.display_sorting_time(end_time - start_time)

    def start_cocktail_sort(self):
        self.shuffle_array()
        start_time = time.time()
        self.cocktail_shaker_sort()
        end_time = time.time()
        self.display_sorting_time(end_time - start_time)

    def start_bogo_sort(self):
        self.shuffle_array()
        start_time = time.time()
        self.bogo_sort()
        end_time = time.time()
        self.display_sorting_time(end_time - start_time)

    def start_grail_sort(self):
        self.shuffle_array()
        start_time = time.time()
        self.grail_sort()
        end_time = time.time()
        self.display_sorting_time(end_time - start_time)


    def odd_even_sort(self):
        n = len(self.arr)
        is_sorted = False
        while not is_sorted:
            is_sorted = True
            for i in range(1, n - 1, 2):  # Odd index pass
                if self.arr[i] > self.arr[i + 1]:
                    self.arr[i], self.arr[i + 1] = self.arr[i + 1], self.arr[i]
                    is_sorted = False
                    self.draw_bars(highlight_indices=[i, i + 1])
                    time.sleep(0.001)

            for i in range(0, n - 1, 2):  # Even index pass
                if self.arr[i] > self.arr[i + 1]:
                    self.arr[i], self.arr[i + 1] = self.arr[i + 1], self.arr[i]
                    is_sorted = False
                    self.draw_bars(highlight_indices=[i, i + 1])
                    time.sleep(0.001)

    def merge(self, left, mid, right):
        L = self.arr[left:mid + 1]
        R = self.arr[mid + 1:right + 1]
        i = j = 0
        k = left

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                self.arr[k] = L[i]
                i += 1
            else:
                self.arr[k] = R[j]
                j += 1
            self.draw_bars(highlight_indices=[k])
            time.sleep(0.001)
            k += 1

        while i < len(L):
            self.arr[k] = L[i]
            i += 1
            k += 1
            self.draw_bars(highlight_indices=[k - 1])
            time.sleep(0.001)

        while j < len(R):
            self.arr[k] = R[j]
            j += 1
            k += 1
            self.draw_bars(highlight_indices=[k - 1])
            time.sleep(0.001)

    def merge_sort(self, left, right):
        if left < right:
            mid = (left + right) // 2
            self.merge_sort(left, mid)
            self.merge_sort(mid + 1, right)
            self.merge(left, mid, right)

    def insertion_sort(self, arr, left, right):
        for i in range(left + 1, right + 1):
            key = arr[i]
            j = i - 1
            while j >= left and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            self.draw_bars(highlight_indices=[i, j + 1])
            time.sleep(0.001)

    def tim_sort(self, run=32):
        n = len(self.arr)
        # Apply insertion sort to small subarrays
        for i in range(0, n, run):
            self.insertion_sort(self.arr, i, min((i + run - 1), n - 1))

        # Start merging the subarrays
        size = run
        while size < n:
            for start in range(0, n, 2 * size):
                mid = min(n - 1, start + size - 1)
                end = min((start + 2 * size - 1), (n - 1))
                if mid < end:
                    self.merge(start, mid, end)
            size = 2 * size

    def quick_sort(self, low, high):
        if low < high:
            pi = self.partition(low, high)
            self.quick_sort(low, pi - 1)  # Before pivot
            self.quick_sort(pi + 1, high)  # After pivot

    def partition(self, low, high):
        pivot = self.arr[high]  # Taking the last element as pivot
        i = low - 1  # Index of the smaller element

        for j in range(low, high):
            if self.arr[j] <= pivot:
                i += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                self.draw_bars(highlight_indices=[i, j])
                time.sleep(0.001)

        # Swap pivot with the element at i + 1
        self.arr[i + 1], self.arr[high] = self.arr[high], self.arr[i + 1]
        self.draw_bars(highlight_indices=[i + 1, high])
        time.sleep(0.001)

        return i + 1  # Return the partitioning index

    def selection_sort(self):
        n = len(self.arr)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if self.arr[j] < self.arr[min_index]:
                    min_index = j
            self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]
            self.draw_bars(highlight_indices=[i, min_index])
            time.sleep(0.001)

    def lsd_radix_sort(self):
        max_val = max(self.arr)  # Find the largest number to determine number of digits
        exp = 1  # Start from the least significant digit

        while max_val // exp > 0:
            self.count_sort_by_digit(exp)
            exp *= 10

    def count_sort_by_digit(self, exp):
        n = len(self.arr)
        output = [0] * n  # Output array
        count = [0] * 10  # Count array for each digit (0-9)

        # Store count of occurrences in count[]
        for i in range(n):
            index = self.arr[i] // exp
            count[index % 10] += 1

        # Change count[i] to contain the actual position of this digit in output[]
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build the output array in sorted order based on the current digit
        for i in range(n - 1, -1, -1):
            index = self.arr[i] // exp
            output[count[index % 10] - 1] = self.arr[i]
            count[index % 10] -= 1

        # Copy the output array to arr[], so that arr[] now contains sorted numbers
        for i in range(n):
            self.arr[i] = output[i]
            self.draw_bars(highlight_indices=[i])
            time.sleep(0.001)

    # Bubble Sort Algorithm
    def bubble_sort(self):
        n = len(self.arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]
                    self.draw_bars(highlight_indices=[j, j+1])
                    time.sleep(0.001)  # Adjust sleep time if needed for speed




    def cocktail_shaker_sort(self):
        n = len(self.arr)
        start = 0
        end = n - 1
        swapped = True
        while swapped:
            swapped = False
            for i in range(start, end):
                if self.arr[i] > self.arr[i + 1]:
                    self.arr[i], self.arr[i + 1] = self.arr[i + 1], self.arr[i]
                    swapped = True
                    self.draw_bars(highlight_indices=[i, i + 1])
                    time.sleep(0.001)
                    
            if not swapped:
                break

            swapped = False
            end -= 1
                        
            for i in range(end - 1, start - 1, -1):
                if self.arr[i] > self.arr[i + 1]:
                    self.arr[i], self.arr[i + 1] = self.arr[i + 1], self.arr[i]
                    swapped = True
                    self.draw_bars(highlight_indices=[i, i + 1])
                    time.sleep(0.001)

            
            start += 1


    import random

    def bogo_sort(self):
        while not self.is_sorted():
            random.shuffle(self.arr)
            self.draw_bars()
            time.sleep(0.1)  # Adjust sleep for speed

    def is_sorted(self):
        for i in range(len(self.arr) - 1):
            if self.arr[i] > self.arr[i + 1]:
                return False
        return True


    def grail_sort(self):
        n = len(self.arr)
        block_size = int(math.sqrt(n))  # Block size is square root of n
        num_blocks = math.ceil(n / block_size)

        # Step 1: Sort each block using insertion sort (or merge sort)
        for i in range(num_blocks):
            start = i * block_size
            end = min((i + 1) * block_size, n)  # Ensure we don't go out of bounds
            self.insertion_sort_grail(start, end - 1)
            self.draw_bars(highlight_indices=range(start, end))
            time.sleep(0.01)

        # Step 2: Perform a multi-way merge in place
        step = block_size
        while step < n:
            for start in range(0, n, 2 * step):
                mid = min(n - 1, start + step - 1)
                end = min(n - 1, start + 2 * step - 1)
                if mid < end:
                    self.merge_in_place(start, mid, end)
            step *= 2
            self.draw_bars()
            time.sleep(0.01)

    # Merge two blocks in-place
    def merge_in_place(self, start, mid, end):
        left = start
        right = mid + 1
        while left <= mid and right <= end:
            if self.arr[left] <= self.arr[right]:
                left += 1
            else:
                # Rotate the block from left to right
                value = self.arr[right]
                self.arr[left + 1:right + 1] = self.arr[left:right]
                self.arr[left] = value
                left += 1
                mid += 1
                right += 1
                self.draw_bars(highlight_indices=[left, right])
                time.sleep(0.01)

    # Insertion Sort (for sorting blocks)
    def insertion_sort_grail(self, start, end):
        for i in range(start + 1, end + 1):
            key = self.arr[i]
            j = i - 1
            while j >= start and self.arr[j] > key:
                self.arr[j + 1] = self.arr[j]
                j -= 1
            self.arr[j + 1] = key
            self.draw_bars(highlight_indices=[i, j + 1])
            time.sleep(0.01)


    



# Run the visualizer
root = tk.Tk()
visualizer = SortVisualizer(root)
root.mainloop()