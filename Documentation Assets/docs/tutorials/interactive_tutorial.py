
from typing import Dict, List
import ipywidgets as widgets
from IPython.display import display, HTML, clear_output

class InteractiveTutorial:
    def __init__(self):
        self.current_step = 0
        self.tutorial_steps = []
        self.feedback_scores = []
        
    def add_step(self, title: str, content: str, code_example: str = None):
        """Add a tutorial step."""
        self.tutorial_steps.append({
            'title': title,
            'content': content,
            'code_example': code_example
        })
        
    def create_quiz(self, question: str, options: List[str], correct_answer: int):
        """Create an interactive quiz."""
        quiz_widget = widgets.RadioButtons(
            options=options,
            description=question,
            disabled=False
        )
        
        def check_answer(change):
            if change['new'] == options[correct_answer]:
                print("Correct! 🎉")
            else:
                print("Try again! 💪")
                
        quiz_widget.observe(check_answer, names='value')
        return quiz_widget
    
    def display_current_step(self):
        """Display current tutorial step."""
        clear_output(wait=True)
        step = self.tutorial_steps[self.current_step]
        
        display(HTML(f"<h2>{step['title']}</h2>"))
        display(HTML(f"<p>{step['content']}</p>"))
        
        if step['code_example']:
            display(HTML(f"<pre><code>{step['code_example']}</code></pre>"))
            
    def create_navigation(self):
        """Create navigation buttons."""
        prev_button = widgets.Button(description='Previous')
        next_button = widgets.Button(description='Next')
        
        def on_prev_click(b):
            if self.current_step > 0:
                self.current_step -= 1
                self.display_current_step()
                
        def on_next_click(b):
            if self.current_step < len(self.tutorial_steps) - 1:
                self.current_step += 1
                self.display_current_step()
                
        prev_button.on_click(on_prev_click)
        next_button.on_click(on_next_click)
        
        return widgets.HBox([prev_button, next_button])
    
    def start_tutorial(self):
        """Start the interactive tutorial."""
        self.display_current_step()
        display(self.create_navigation())
