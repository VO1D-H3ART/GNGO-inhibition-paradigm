import pygame
import random
import time
import sys
import os


## initialtizes the screen and draws 800,600 display.
pygame.init()
screen=pygame.display.set_mode((800, 600))
pygame.display.set_caption('G-NGO Paradigm')


base_dir = os.path.join(os.path.dirname(__file__), 'Images')

#Image set, Sample folder provided on sources jpg folder, small cross and triangle no Gos for this setting
images=[os.path.join(base_dir, 'image1.jpg'),
        os.path.join(base_dir, 'image2.jpg'),
        os.path.join(base_dir, 'image3.jpg'),
        os.path.join(base_dir, 'image4.jpg'),
        os.path.join(base_dir, 'image5.jpg'),
        os.path.join(base_dir, 'image6.jpg'),
        os.path.join(base_dir, 'image7.jpg'),
        os.path.join(base_dir, 'image8.jpg')]

no_go_images=[os.path.join(base_dir, 'image6.jpg'),
              os.path.join(base_dir, 'image8.jpg')]

loaded_images={img: pygame.image.load(img) for img in images}

###########Paradigm parameters###############

#Display time for each stimulus
DISPLAY_TIME = 0.2

#Interstimulus interval
ISI_TIME = 1.3

#Total number of stimuli trials
TOTAL_TRIALS = 150


def run_experiment():
    #random pick of 150 trials amongst the images
    stim_order = random.choices(images, k=TOTAL_TRIALS) 
    
    for stimulus in stim_order:
        
        # Display the stimulus (currently set as random)
        screen.blit(loaded_images[stimulus], (350, 250)) #This is where the image is displayed, as the display is 800x600 and image is 100x1000: Center of Screen: (800/2, 600/2) = (400, 300), edit accordingly if you change!!
        pygame.display.flip()
        start_time = time.time()

        # Handle stimulus display duration
        while time.time() - start_time < DISPLAY_TIME:  # 200 ms stimulus display

            ##Game Heart
            for event in pygame.event.get():

                ##kills game
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    # Handle response logic here
                    pass

        # Display blank screen during isi
        screen.fill((0, 0, 0)) ##color of the background
        pygame.display.flip()
        time.sleep(ISI_TIME)


 
run_experiment()

