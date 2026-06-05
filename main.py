"""
GhostForge IDE - Kivy Version
Simple, clean, working version
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.core.window import Window
import subprocess
from pathlib import Path

# Window setup
Window.size = (480, 800)

class GhostForgeApp(App):
    """Main application"""
    
    def build(self):
        """Build the UI"""
        
        # Main layout
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Header
        header = Label(
            text='🔥 GhostForge IDE',
            size_hint_y=0.08,
            font_size='20sp'
        )
        main_layout.add_widget(header)
        
        # Tabs
        tabs = TabbedPanel(size_hint_y=0.92)
        
        # ============================================================
        # TAB 1: CHAT
        # ============================================================
        tab_chat = TabbedPanelItem(text='🤖 Chat')
        
        chat_layout = BoxLayout(orientation='vertical', padding=5, spacing=5)
        
        # Chat output
        self.chat_output = Label(
            text='Chat with AI\n\nHello! How can I help?',
            size_hint_y=0.7
        )
        chat_scroll = ScrollView()
        chat_scroll.add_widget(self.chat_output)
        chat_layout.add_widget(chat_scroll)
        
        # Chat input
        chat_input_layout = BoxLayout(size_hint_y=0.3, spacing=5)
        self.chat_input = TextInput(
            text='',
            multiline=False,
            size_hint_x=0.8
        )
        chat_input_layout.add_widget(self.chat_input)
        
        chat_send = Button(text='Send', size_hint_x=0.2)
        chat_send.bind(on_press=self.chat_send)
        chat_input_layout.add_widget(chat_send)
        
        chat_layout.add_widget(chat_input_layout)
        tab_chat.content = chat_layout
        tabs.add_widget(tab_chat)
        
        # ============================================================
        # TAB 2: TERMINAL
        # ============================================================
        tab_terminal = TabbedPanelItem(text='💻 Terminal')
        
        terminal_layout = BoxLayout(orientation='vertical', padding=5, spacing=5)
        
        # Terminal output
        self.terminal_output = Label(
            text='$ Terminal\n\nReady...',
            size_hint_y=0.7
        )
        terminal_scroll = ScrollView()
        terminal_scroll.add_widget(self.terminal_output)
        terminal_layout.add_widget(terminal_scroll)
        
        # Terminal input
        terminal_input_layout = BoxLayout(size_hint_y=0.3, spacing=5)
        self.terminal_input = TextInput(
            text='',
            multiline=False,
            size_hint_x=0.8
        )
        terminal_input_layout.add_widget(self.terminal_input)
        
        terminal_run = Button(text='Run', size_hint_x=0.2)
        terminal_run.bind(on_press=self.terminal_run)
        terminal_input_layout.add_widget(terminal_run)
        
        terminal_layout.add_widget(terminal_input_layout)
        tab_terminal.content = terminal_layout
        tabs.add_widget(tab_terminal)
        
        # ============================================================
        # TAB 3: EDITOR
        # ============================================================
        tab_editor = TabbedPanelItem(text='📝 Editor')
        
        editor_layout = BoxLayout(orientation='vertical', padding=5, spacing=5)
        
        # Code editor
        self.code_editor = TextInput(
            text='# Write your code here\n',
            multiline=True
        )
        editor_layout.add_widget(self.code_editor)
        
        # Buttons
        button_layout = BoxLayout(size_hint_y=0.1, spacing=5)
        
        save_btn = Button(text='Save')
        save_btn.bind(on_press=self.save_code)
        button_layout.add_widget(save_btn)
        
        build_btn = Button(text='Build APK')
        build_btn.bind(on_press=self.build_apk)
        button_layout.add_widget(build_btn)
        
        editor_layout.add_widget(button_layout)
        tab_editor.content = editor_layout
        tabs.add_widget(tab_editor)
        
        # ============================================================
        # TAB 4: BUILD
        # ============================================================
        tab_build = TabbedPanelItem(text='🔨 Build')
        
        build_layout = BoxLayout(orientation='vertical', padding=5, spacing=5)
        
        self.build_output = Label(
            text='Build output appears here\n\nReady to build...',
            size_hint_y=1.0
        )
        build_scroll = ScrollView()
        build_scroll.add_widget(self.build_output)
        build_layout.add_widget(build_scroll)
        
        tab_build.content = build_layout
        tabs.add_widget(tab_build)
        
        # ============================================================
        # TAB 5: FILES
        # ============================================================
        tab_files = TabbedPanelItem(text='📦 Files')
        
        files_layout = BoxLayout(orientation='vertical', padding=5, spacing=5)
        
        self.files_output = Label(
            text='Files appear here\n\nRefresh to see files...',
            size_hint_y=0.9
        )
        files_scroll = ScrollView()
        files_scroll.add_widget(self.files_output)
        files_layout.add_widget(files_scroll)
        
        refresh_btn = Button(text='Refresh', size_hint_y=0.1)
        refresh_btn.bind(on_press=self.refresh_files)
        files_layout.add_widget(refresh_btn)
        
        tab_files.content = files_layout
        tabs.add_widget(tab_files)
        
        main_layout.add_widget(tabs)
        
        return main_layout
    
    def chat_send(self, instance):
        """Send chat message"""
        msg = self.chat_input.text
        if not msg:
            return
        
        self.chat_output.text += f"\n\nYou: {msg}\n\nAI: Got your message!"
        self.chat_input.text = ''
    
    def terminal_run(self, instance):
        """Run terminal command"""
        cmd = self.terminal_input.text
        if not cmd:
            return
        
        try:
            result = subprocess.run(
                cmd,
                shell=True,
                capture_output=True,
                text=True,
                timeout=10
            )
            output = result.stdout + result.stderr
            self.terminal_output.text += f"\n$ {cmd}\n{output}"
        except Exception as e:
            self.terminal_output.text += f"\n$ {cmd}\nError: {str(e)}"
        
        self.terminal_input.text = ''
    
    def save_code(self, instance):
        """Save code"""
        try:
            code_dir = Path.home() / "GhostForge"
            code_dir.mkdir(exist_ok=True)
            
            file_path = code_dir / "code.py"
            file_path.write_text(self.code_editor.text)
            
            self.build_output.text = f"✅ Saved to {file_path}"
        except Exception as e:
            self.build_output.text = f"❌ Error: {str(e)}"
    
    def build_apk(self, instance):
        """Build APK"""
        self.build_output.text = "🔨 Building APK...\n\nThis would run buildozer android release\n\nNote: Actual build requires full Android SDK/NDK setup"
    
    def refresh_files(self, instance):
        """Refresh files"""
        try:
            code_dir = Path.home() / "GhostForge"
            if code_dir.exists():
                files = list(code_dir.glob("*"))
                files_text = "Files in ~/GhostForge:\n\n"
                for f in files:
                    files_text += f"📄 {f.name}\n"
                self.files_output.text = files_text
            else:
                self.files_output.text = "No files yet"
        except Exception as e:
            self.files_output.text = f"Error: {str(e)}"


if __name__ == '__main__':
    GhostForgeApp().run()
