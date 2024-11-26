import pygame
import pygame_gui
import random
import time
import math


# Screen and bar colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BAR_COLOR = (255, 255, 255)

# Define display dimensions
WIDTH, HEIGHT = 800, 600
BAR_WIDTH = 5
BOTTOM_GUI_HEIGHT = 100  # Height for the bottom GUI section

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT + BOTTOM_GUI_HEIGHT))
pygame.display.set_caption("Sorting Algorithm Visualizer")
manager = pygame_gui.UIManager((WIDTH, HEIGHT + BOTTOM_GUI_HEIGHT))


class SortVisualizer:
    def __init__(self):
        self.array_size = 100 # Start with a default size
        self.array = list(range(1, self.array_size + 1))
        self.array_len = len(self.array)
        self.algo_name = "None"
        self.start_time = 0
        self.elapsed_time = 0
        self.is_sorting = False
        
        # Initialize array_writes before shuffle_array()
        self.array_writes = 0  # Track array writes

        self.shuffle_array()

        # Create the slider
        self.slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect((WIDTH - 310, 10), (300, 20)),
            start_value=self.array_size,
            value_range=(5, 800),
            manager=manager
        )
        self.force_quit_button = None
        
    def reset_write_count(self):
        self.array_writes = 0

    def array_write(self, index, value):
        """Controlled array write method to track writes"""
        self.array[index] = value
        self.array_writes += 1

    def update_array_size(self, new_size):
        self.array_size = max(2, min(new_size, 800))
        self.array = list(range(1, self.array_size + 1))
        self.array_len = len(self.array)
        self.shuffle_array()

    def start_sort(self, sort_function):
        self.reset_write_count()  # Reset array writes count for new sort
        self.shuffle_array()  # Shuffle array before each new sort
        self.is_sorting = True
        self.start_time = time.time()
        sort_function()  # Run the sorting algorithm
        self.elapsed_time = time.time() - self.start_time
        self.is_sorting = False
        self.draw_bars()  # Final update to show completion time




    def shuffle_array(self):
        random.shuffle(self.array)
        self.draw_bars()

    def draw_bars(self, highlighted_indices=None):
        screen.fill(BLACK)
        font = pygame.font.SysFont(None, 30)
        
        # Draw algorithm name
        algo_text = font.render(f"Algorithm: {self.algo_name}", True, WHITE)
        screen.blit(algo_text, (10, 10))
        
        # Draw timer
        if self.is_sorting:
            current_time = time.time() - self.start_time
        else:
            current_time = self.elapsed_time
        
        timer_text = font.render(f"Time: {current_time:.2f} seconds", True, WHITE)
        screen.blit(timer_text, (10, 40))

        # Draw array size label
        size_text = font.render(f"Array Size: {self.array_size}", True, WHITE)
        screen.blit(size_text, (10, 70))

        # Calculate bar dimensions to fill screen width
        padding_top = 100  # Space for text at top
        padding_bottom = 50  # Space at bottom
        available_height = HEIGHT - padding_top - padding_bottom
        
        # Calculate bar width to fill entire screen width
        bar_width = WIDTH / self.array_size  # Divide full width by number of bars
        
        # Scale heights to fill available vertical space
        max_value = max(self.array)
        height_scale = available_height / max_value

        writes_text = font.render(f"Array Writes: {self.array_writes}", True, WHITE)
        screen.blit(writes_text, (10, 100))

        for i, value in enumerate(self.array):
            # Calculate bar position and dimensions
            x = i * bar_width
            bar_height = value * height_scale
            y = HEIGHT - padding_bottom - bar_height

            # Draw bar
            if highlighted_indices and i in highlighted_indices:
                color = (255, 0, 0)  # Red for highlighted bars
            else:
                color = BAR_COLOR
                
            # Draw bar with no gaps
            pygame.draw.rect(screen, color, (x, y, bar_width, bar_height))

        self.draw_gui()
        pygame.display.flip()



    def draw_gui(self):
        font = pygame.font.SysFont(None, 24)
        manager.draw_ui(screen)
        instructions_left = [
            "Hotkeys for Algorithms:",
            "I - Insertion Sort",
            "B - Bubble Sort",
            "S - Selection Sort"
        ]
        instructions_middle = [
            "O - Bogo Sort",
            "H - Heap Sort",  # Suggest adding Heap Sort
            "C - Cocktail Sort"  # Suggest adding Cocktail Sort
        ]
        instructions_right = [
            "Q - Quick Sort",
            "M - Merge Sort",
            "G - Grail Sort",
            "R - Reset / Shuffle Array"
        ]

        # Positioning parameters
        x_offset_left = 20
        x_offset_middle = WIDTH // 3 + 20
        x_offset_right = WIDTH - 250
        y_offset = HEIGHT + 10

        # Render and blit instructions for left column
        for instruction in instructions_left:
            text_surface = font.render(instruction, True, WHITE)
            screen.blit(text_surface, (x_offset_left, y_offset))
            y_offset += 20

        # Reset y_offset for middle column
        y_offset = HEIGHT + 10

        # Render and blit instructions for middle column
        for instruction in instructions_middle:
            text_surface = font.render(instruction, True, WHITE)
            screen.blit(text_surface, (x_offset_middle, y_offset))
            y_offset += 20

        # Reset y_offset for right column
        y_offset = HEIGHT + 10

        # Render and blit instructions for right column
        for instruction in instructions_right:
            text_surface = font.render(instruction, True, WHITE)
            screen.blit(text_surface, (x_offset_right, y_offset))
            y_offset += 20

    # Add a force quit button
        self.force_quit_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((WIDTH - 100, HEIGHT + BOTTOM_GUI_HEIGHT - 100), (90, 30)),
            text='Force Quit',
            manager=manager
        )

    def set_algorithm(self, algo_name):
        self.algo_name = algo_name
        self.draw_bars()  # Update the display with the new algorithm name

    def bubble_sort(self):
        self.reset_write_count()
        self.set_algorithm("Bubble Sort")
        n = len(self.array)
        for i in range(n):
            for j in range(0, n - i - 1):
                pygame.event.pump()  # Allow Pygame to process events
                if self.array[j] > self.array[j + 1]:
                    temp = self.array[j]
                    self.array_write(j, self.array[j + 1])
                    self.array_write(j + 1, temp)
                    self.draw_bars([j, j + 1])
                    pygame.display.flip()  # Refresh display
                    time.sleep(0.01)

    def selection_sort(self):
        self.reset_write_count()
        self.set_algorithm("Selection Sort")
        n = len(self.array)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                pygame.event.pump()
                if self.array[j] < self.array[min_index]:
                    min_index = j
            temp = self.array[i]
            self.array_write(i, self.array[min_index])
            self.array_write(min_index, temp)
            self.draw_bars([i, min_index])
            pygame.display.flip()
            time.sleep(0.01)

    def quick_sort(self):
        self.reset_write_count()
        self.set_algorithm("Quick Sort")

        def partition(low, high):
            pivot = self.array[high]
            i = low - 1

            for j in range(low, high):
                pygame.event.pump()  # Allow Pygame to process events
                if self.array[j] <= pivot:
                    i += 1
                    # Swap elements and update the display
                    temp = self.array[i]
                    self.array_write(i, self.array[j])
                    self.array_write(j, temp)
                    self.draw_bars([i, j])
                    pygame.display.flip()
                    time.sleep(0.01)

            # Swap pivot to correct position
            self.array[i + 1], self.array[high] = self.array[high], self.array[i + 1]
            self.draw_bars([i + 1, high])
            pygame.display.flip()
            time.sleep(0.01)

            return i + 1

        def quick_sort_recursive(low, high):
            if low < high:
                pi = partition(low, high)
                quick_sort_recursive(low, pi - 1)
                quick_sort_recursive(pi + 1, high)

        quick_sort_recursive(0, len(self.array) - 1)


    def merge_sort(self):
        self.reset_write_count()
        self.set_algorithm("Merge Sort")
        
        def merge(start, mid, end):
            # In-place merge using only the main array
            left = start
            right = mid + 1
            
            # If already sorted, no need to merge
            if self.array[mid] <= self.array[right]:
                return
            
            while left <= mid and right <= end:
                pygame.event.pump()
                
                if self.array[left] <= self.array[right]:
                    left += 1
                else:
                    # Rotate the elements
                    temp = self.array[right]
                    
                    # Shift elements to the right
                    for i in range(right, left, -1):
                        self.array_write(i, self.array[i-1])
                    
                    # Insert the temp element
                    self.array_write(left, temp)
                    
                    left += 1
                    mid += 1
                    right += 1
                    
                    self.draw_bars(highlighted_indices=[left-1, right-1])
                    pygame.display.flip()
                    time.sleep(0.01)
        
        def merge_sort_recursive(start, end):
            if start >= end:
                return
            
            mid = (start + end) // 2
            merge_sort_recursive(start, mid)
            merge_sort_recursive(mid + 1, end)
            merge(start, mid, end)
        
        merge_sort_recursive(0, len(self.array) - 1)

    def insertion_sort(self):
            self.reset_write_count()
            self.set_algorithm("Insertion Sort")
            for i in range(1, len(self.array)):
                key = self.array[i]
                j = i - 1
                while j >= 0 and key < self.array[j]:
                    pygame.event.pump()
                    self.array_write(j + 1, self.array[j])
                    j -= 1
                    self.draw_bars([j, j + 1])
                    pygame.display.flip()
                    time.sleep(0.01)
                self.array_write(j + 1, key)
                self.draw_bars([j + 1])

    def grail_sort(self):
        self.reset_write_count()
        self.set_algorithm("Grail Sort")
        n = len(self.array)
        if n <= 1:
            return
            
        block_size = max(1, int(math.sqrt(n)))
        num_blocks = math.ceil(n / block_size)

        try:
            # Step 1: Sort each block using insertion sort
            for i in range(num_blocks):
                pygame.event.pump()  # Allow pygame to process events
                start = i * block_size
                end = min((i + 1) * block_size, n)
                self.insertion_sort_grail(start, end - 1)
                self.draw_bars(highlighted_indices=range(start, end))
                time.sleep(0.01)

            # Step 2: Perform a multi-way merge in place
            step = block_size
            while step < n:
                pygame.event.pump()  # Allow pygame to process events
                for start in range(0, n, 2 * step):
                    mid = min(start + step - 1, n - 1)
                    end = min(start + 2 * step - 1, n - 1)
                    if mid < end:
                        self.merge_in_place(start, mid, end)
                step *= 2
                self.draw_bars()
                time.sleep(0.01)
        except Exception as e:
            print(f"Error in grail sort: {e}")

    def merge_in_place(self, start, mid, end):
        left = start
        right = mid + 1
        
        # Only proceed if there are elements to merge
        while left <= mid and right <= end:
            pygame.event.pump()  # Allow pygame to process events
            
            if self.array[left] <= self.array[right]:
                left += 1
            else:
                value = self.array[right]
                # Make sure we don't exceed array bounds
                if left < right:
                    # Shift elements only within valid bounds
                    for i in range(right, left, -1):
                        self.array_write(i, self.array[i - 1])
                    self.array_write(left, value)
                    
                left += 1
                mid += 1
                right += 1
                
                self.draw_bars(highlighted_indices=[left-1, right-1])
                pygame.display.flip()
                time.sleep(0.01)

    # Insertion Sort (for sorting blocks)
    def insertion_sort_grail(self, start, end):
        for i in range(start + 1, end + 1):
            key = self.array[i]
            j = i - 1
            while j >= start and self.array[j] > key:
                self.array_write(j + 1, self.array[j])
                j -= 1
            self.array_write(j + 1, key)
            # Highlight the bars that are being compared/swapped
            self.draw_bars(highlighted_indices=[i, j + 1])
            time.sleep(0.01)

    def bogo_sort(self):
        self.reset_write_count()
        self.set_algorithm("Bogo Sort")
        
        def is_sorted():
            for i in range(1, len(self.array)):
                if self.array[i] < self.array[i-1]:
                    return False
            return True
        
        attempts = 0        
        while not is_sorted():
            pygame.event.pump()  # Allow Pygame to process events
            
            # Randomly shuffle the array
            random.shuffle(self.array)
            attempts += 1
            
            # Update visualization
            self.draw_bars()
            pygame.display.flip()
            time.sleep(0.1)  # Slow down visualization

def main():
    running = True
    visualizer = SortVisualizer()
    clock = pygame.time.Clock()

    while running:
        time_delta = clock.tick(60)/1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == visualizer.force_quit_button:
                    running = False
                    pygame.quit()
                    return
            if event.type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                if event.ui_element == visualizer.slider:
                    new_size = int(event.value)
                    visualizer.update_array_size(new_size)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    visualizer.start_sort(visualizer.insertion_sort)
                elif event.key == pygame.K_b:
                    visualizer.start_sort(visualizer.bubble_sort)
                elif event.key == pygame.K_s:
                    visualizer.start_sort(visualizer.selection_sort)
                elif event.key == pygame.K_q:
                    visualizer.start_sort(visualizer.quick_sort)
                elif event.key == pygame.K_o:
                    visualizer.start_sort(visualizer.bogo_sort)
                elif event.key == pygame.K_m:
                    visualizer.start_sort(visualizer.merge_sort)
                elif event.key == pygame.K_g:
                    visualizer.start_sort(visualizer.grail_sort)
                elif event.key == pygame.K_r:
                    visualizer.shuffle_array()
                    visualizer.elapsed_time = 0

            manager.process_events(event)

        manager.update(time_delta)
        visualizer.draw_bars()
        pygame.display.flip()

    pygame.quit()
if __name__ == "__main__":
    main()
