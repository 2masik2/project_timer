import pygame
import time

pygame.init()

#определяем размеры окна
window_width = 700
window_height = 500

#определение цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
clock = pygame.time.Clock()
#создаем окно
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Секундомер")
pygame.font.init()



#создаем шрифты для отображения времени
sign_font = pygame.font.SysFont(None, 28)
stopwatch_font = pygame.font.SysFont(None, 48)


#определяем время секундомера
stopwatch_start = None
stopwatch_elapsed_time = 0
stopwatch_running = False


#создаем основной цикл программы 
while True:
    #обрабатываем события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not stopwatch_running:
                    stopwatch_start = time.time()
                    stopwatch_running = True
                else:
                    stopwatch_running = False


    #очищаем экран
    screen.fill(BLACK)


    #обновляем секунодмер
    if stopwatch_running:
        stopwatch_elapsed_time = time.time() - stopwatch_start
        stopwatch_text = stopwatch_font.render(f"Секундомер:{stopwatch_elapsed_time:.1f}", True, WHITE)
        screen.blit(stopwatch_text, (200, window_height - stopwatch_text.get_height() - 300))

        #отображаем инструкцию
        instruction_text = sign_font.render("Нажмите пробел для запуска/паузы/сброса секундомера", True, WHITE)
        screen.blit(instruction_text, (100, 100))

        #обновляем экран
        pygame.display.update()