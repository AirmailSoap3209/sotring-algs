import pygame
import pygame_gui
import random
import time

# Colors and display settings
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BAR_COLOR = (255, 255, 255)
WIDTH, HEIGHT = 800, 600
BOTTOM_GUI_HEIGHT = 100

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT + BOTTOM_GUI_HEIGHT))
pygame.display.set_caption("Stalin Sort Visualizer")
manager = pygame_gui.UIManager((WIDTH, HEIGHT + BOTTOM_GUI_HEIGHT))

class StalinSortVisualizer:
    def __init__(self):
        self.array_size = 100
        self.array = list(range(1, self.array_size + 1))
        self.is_sorting = False
        self.start_time = 0
        self.elapsed_time = 0
        self.shuffle_array()

        # Create UI components
        self.slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect((WIDTH - 310, 10), (300, 20)),
            start_value=self.array_size,
            value_range=(5, 800),
            manager=manager
        )
        self.force_quit_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((WIDTH - 100, HEIGHT + BOTTOM_GUI_HEIGHT - 50), (90, 30)),
            text='Force Quit',
            manager=manager
        )

    def shuffle_array(self):
        random.shuffle(self.array)
        self.draw_bars()

    def draw_bars(self, highlighted_indices=None):
        screen.fill(BLACK)
        font = pygame.font.SysFont(None, 30)
        
        # Draw timer
        if self.is_sorting:
            current_time = time.time() - self.start_time
        else:
            current_time = self.elapsed_time
        
        timer_text = font.render(f"Time: {current_time:.2f} seconds", True, WHITE)
        screen.blit(timer_text, (10, 10))

        # Draw array size label
        size_text = font.render(f"Array Size: {self.array_size}", True, WHITE)
        screen.blit(size_text, (10, 40))

        # Bar dimensions and scaling
        padding_top = 100
        padding_bottom = 50
        available_height = HEIGHT - padding_top - padding_bottom
        bar_width = WIDTH / self.array_size
        max_value = max(self.array)
        height_scale = available_height / max_value

        for i, value in enumerate(self.array):
            x = i * bar_width
            bar_height = value * height_scale
            y = HEIGHT - padding_bottom - bar_height
            color = (255, 0, 0) if highlighted_indices and i in highlighted_indices else BAR_COLOR
            pygame.draw.rect(screen, color, (x, y, bar_width, bar_height))

        manager.draw_ui(screen)
        pygame.display.flip()

    def update_array_size(self, new_size):
        self.array_size = max(2, min(new_size, 800))
        self.array = list(range(1, self.array_size + 1))
        self.shuffle_array()

    def stalin_sort(self):
        def stalin_sort_with_reentry(arr):
            red_army = []
            gulag_list = []

            # Send soldiers out of order to gulag
            for value in arr:
                if not red_army or red_army[-1] <= value:
                    red_army.append(value)
                else:
                    gulag_list.append(value)

                # Visualize the current state
                self.draw_bars()
                time.sleep(0.05)  # Slow down to make visualization clearer

            # If no soldiers in gulag, return sorted army
            if not gulag_list:
                return red_army

            # Recursively sort gulag list and merge back
            reentry_army = stalin_sort_with_reentry(gulag_list)
            functioning_army = []

            sorted_idx = 0
            remaining_idx = 0

            # Merge soldiers back into army
            while (sorted_idx < len(red_army)) and (remaining_idx < len(reentry_army)):
                if reentry_army[remaining_idx] < red_army[sorted_idx]:
                    functioning_army.append(reentry_army[remaining_idx])
                    remaining_idx += 1
                else:
                    functioning_army.append(red_army[sorted_idx])
                    sorted_idx += 1

                # Visualize merging process
                self.draw_bars()
                time.sleep(0.05)

            # Add remaining soldiers to end of army
            if (remaining_idx < len(reentry_army)) and (sorted_idx == len(red_army)):
                functioning_army.extend(reentry_army[remaining_idx:])

            if (sorted_idx < len(red_army)) and (remaining_idx == len(reentry_army)):
                functioning_army.extend(red_army[sorted_idx:])

            return functioning_army

        self.is_sorting = True
        self.start_time = time.time()
        
        # Perform Stalin Sort with reentry
        self.array = stalin_sort_with_reentry(self.array)
        
        self.elapsed_time = time.time() - self.start_time
        self.is_sorting = False
        self.draw_bars()

    def merge_sorted_lists(self, sorted_list, gulag_list):
        merged = []
        i, j = 0, 0

        # Merge the two lists in sorted order
        while i < len(sorted_list) and j < len(gulag_list):
            if gulag_list[j] < sorted_list[i]:
                merged.append(gulag_list[j])
                j += 1
            else:
                merged.append(sorted_list[i])
                i += 1

        # Add any remaining elements from both lists
        merged.extend(gulag_list[j:])
        merged.extend(sorted_list[i:])
        
        return merged

def main():
    running = True
    visualizer = StalinSortVisualizer()
    clock = pygame.time.Clock()

    while running:
        time_delta = clock.tick(60) / 1000.0
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
                if event.key == pygame.K_r:
                    visualizer.shuffle_array()
                    visualizer.elapsed_time = 0
                elif event.key == pygame.K_s:
                    visualizer.stalin_sort()

            manager.process_events(event)

        manager.update(time_delta)
        visualizer.draw_bars()
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
