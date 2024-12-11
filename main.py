from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivy.uix.image import Image

# Module Arrays
community_modules = [
    "Discuss", "Calendar", "To-do", "Members", "Contacts", "CRM", "Sales",
    "Dashboards", "Point of Sale", "Invoicing", "Project", "Timesheets",
    "Website", "eLearning", "Email Marketing", "SMS Marketing", "Events",
    "Surveys", "Purchase", "Inventory", "Manufacturing", "Maintenance",
    "Repairs", "Employees", "Attendances", "Recruitment", "Fleet", "Time Off",
    "Expenses", "Lunch", "Live Chat", "Data Cleaning", "Apps", "Settings", "Tests"
]

enterprise_modules = community_modules + [
    "Knowledge", "Meeting Rooms", "Frontdesk", "Appointments", "Subscriptions", "Rental", 
    "Kitchen Display", "Accounting", "Documents", "Field Service", "Planning", "Helpdesk", 
    "Social Marketing", "Marketing Automation", "Quality", "Barcode", "PLM", "Consolidation", 
    "Sign", "Payroll", "Appraisals", "Referrals", "Approvals", "Whatsapp", "IoT", "Apps", 
    "Settings", "Tests", "Attendances", "Recruitment", "Fleet", "Time off", "Expenses", 
    "Lunch", "Live Chat", "Data cleaning"
]

class ModuleSearchApp(MDApp):
    def build(self):
        # Set the window size (optional, just to make it look better)
        Window.size = (400, 600)

        # Set the theme to light initially
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"  # Set to Light mode by default

        # Main Layout
        self.layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20)

        # Input Field
        self.input_field = MDTextField(
            hint_text="Enter module name",
            size_hint=(1, 0.1),
            mode="rectangle"
        )
        self.layout.add_widget(self.input_field)

        # Search Button
        search_button = MDRaisedButton(
            text="Search",
            size_hint=(1, 0.1),
            md_bg_color=self.theme_cls.primary_color,
            on_release=self.search_module
        )
        self.layout.add_widget(search_button)

        # Result Label
        self.result_label = MDLabel(
            text="",
            size_hint=(1, 0.2),
            halign="center",
            theme_text_color="Primary"
        )
        self.layout.add_widget(self.result_label)

        # Result Image (for tick/cross)
        self.result_image = Image(size_hint=(None, None), size=(50, 50))  # Use kivy.uix.image.Image
        self.layout.add_widget(self.result_image)

        # Theme Toggle Button with Sun and Moon Icons
        self.theme_toggle_button = MDRaisedButton(
            text="Dark Mode",
            size_hint=(None, None),
            size=(200, 50),  # Make the button smaller
            md_bg_color=self.theme_cls.primary_color,
            on_release=self.toggle_theme
        )
        self.theme_toggle_button.icon = "weather-sunny" if self.theme_cls.theme_style == "Light" else "weather-night"
        self.layout.add_widget(self.theme_toggle_button)

        return self.layout

    def search_module(self, instance):
        # Get the entered module name, convert to lowercase
        module_name = self.input_field.text.strip().lower()

        # Perform case-insensitive comparison
        if not module_name:
            self.result_label.text = "Please enter a module name."
            self.result_image.source = ""
        elif module_name in [module.lower() for module in community_modules] and module_name in [module.lower() for module in enterprise_modules]:
            self.result_label.text = f"{module_name} is available in both Community and Enterprise."
            self.result_image.source = "check_icon.png"  # Path to checkmark image
        elif module_name in [module.lower() for module in community_modules]:
            self.result_label.text = f"{module_name} is available in Community only."
            self.result_image.source = "check_icon.png"  # Path to checkmark image
        elif module_name in [module.lower() for module in enterprise_modules]:
            self.result_label.text = f"{module_name} is available in Enterprise only."
            self.result_image.source = "check_icon.png"  # Path to checkmark image
        else:
            self.result_label.text = f"{module_name} is not available in either Community or Enterprise."
            self.result_image.source = "cross_icon.png"  # Path to cross icon

    def toggle_theme(self, instance):
        if self.theme_cls.theme_style == "Light":
            # Switch to Dark Mode
            self.theme_cls.theme_style = "Dark"
            self.result_image.source = "moon.png"  # Use moon icon for dark mode
            instance.icon = "weather-night"  # Change icon to moon
        else:
            # Switch to Light Mode
            self.theme_cls.theme_style = "Light"
            self.result_image.source = "sun.png"  # Use sun icon for light mode
            instance.icon = "weather-sunny"  # Change icon to sun

if __name__ == "__main__":
    ModuleSearchApp().run()


# from kivymd.app import MDApp
# from kivymd.uix.boxlayout import MDBoxLayout
# from kivymd.uix.textfield import MDTextField
# from kivymd.uix.button import MDRaisedButton
# from kivymd.uix.label import MDLabel
# from kivy.uix.switch import Switch  # Use Kivy's Switch instead of MDSwitch
# from kivy.uix.image import Image  # Use Kivy's Image instead of kivymd.uix.image
# from kivy.core.window import Window

# # Module Arrays
# community_modules = [
#     "Discuss", "Calendar", "To-do", "Members", "Contacts", "CRM", "Sales",
#     "Dashboards", "Point of Sale", "Invoicing", "Project", "Timesheets",
#     "Website", "eLearning", "Email Marketing", "SMS Marketing", "Events",
#     "Surveys", "Purchase", "Inventory", "Manufacturing", "Maintenance",
#     "Repairs", "Employees", "Attendances", "Recruitment", "Fleet", "Time Off",
#     "Expenses", "Lunch", "Live Chat", "Data Cleaning", "Apps", "Settings", "Tests"
# ]

# enterprise_modules = community_modules + [
#     "Knowledge", "Meeting Rooms", "Frontdesk", "Appointments", "Subscriptions",
#     "Rental", "Kitchen Display", "Accounting", "Documents", "Field Service",
#     "Planning", "Helpdesk", "Social Marketing", "Marketing Automation",
#     "Quality", "Barcode", "PLM", "Consolidation", "Sign", "Payroll",
#     "Appraisals", "Referrals", "Approvals", "Whatsapp", "IoT"
# ]

# class ModuleSearchApp(MDApp):
#     def build(self):
#         # Set the window size (optional, just to make it look better)
#         Window.size = (400, 600)

#         # Set the theme to light initially
#         self.theme_cls.primary_palette = "Blue"
#         self.theme_cls.theme_style = "Light"  # Set to Light mode by default

#         # Main Layout
#         self.layout = MDBoxLayout(orientation='vertical', padding=20, spacing=20)

#         # Input Field
#         self.input_field = MDTextField(
#             hint_text="Enter module name",
#             size_hint=(1, 0.1),
#             mode="rectangle"
#         )
#         self.layout.add_widget(self.input_field)

#         # Search Button
#         search_button = MDRaisedButton(
#             text="Search",
#             size_hint=(1, 0.1),
#             md_bg_color=self.theme_cls.primary_color,
#             on_release=self.search_module
#         )
#         self.layout.add_widget(search_button)

#         # Result Label
#         self.result_label = MDLabel(
#             text="",
#             size_hint=(1, 0.2),
#             halign="center",
#             theme_text_color="Primary"
#         )
#         self.layout.add_widget(self.result_label)

#         # Result Image (for tick/cross)
#         self.result_image = Image(size_hint=(None, None), size=(50, 50))  # Use kivy.uix.image.Image
#         self.layout.add_widget(self.result_image)

#         # Theme Toggle Button with Sun and Moon Icons
#         self.theme_toggle_button = MDRaisedButton(
#             text="Dark Mode",
#             size_hint=(1, 0.1),
#             icon="weather-sunny" if self.theme_cls.theme_style == "Light" else "weather-night",
#             md_bg_color=self.theme_cls.primary_color,
#             on_release=self.toggle_theme
#         )
#         self.layout.add_widget(self.theme_toggle_button)

#         return self.layout

#     def search_module(self, instance):
#         # Get the entered module name, convert to lowercase
#         module_name = self.input_field.text.strip().lower()

#         # Perform case-insensitive comparison
#         if not module_name:
#             self.result_label.text = "Please enter a module name."
#             self.result_image.source = ""
#         elif module_name in [module.lower() for module in community_modules] and module_name in [module.lower() for module in enterprise_modules]:
#             self.result_label.text = f"{module_name} is available in both Community and Enterprise."
#             self.result_image.source = "check_icon.png"  # Path to checkmark image
#         elif module_name in [module.lower() for module in community_modules]:
#             self.result_label.text = f"{module_name} is available in Community only."
#             self.result_image.source = "check_icon.png"  # Path to checkmark image
#         elif module_name in [module.lower() for module in enterprise_modules]:
#             self.result_label.text = f"{module_name} is available in Enterprise only."
#             self.result_image.source = "check_icon.png"  # Path to checkmark image
#         else:
#             self.result_label.text = f"{module_name} is not available in either Community or Enterprise."
#             self.result_image.source = "cross_icon.png"  # Path to cross icon

#     def toggle_theme(self, instance):
#         if self.theme_cls.theme_style == "Light":
#             # Switch to Dark Mode
#             self.theme_cls.theme_style = "Dark"
#             self.theme_toggle_button.icon = "weather-night"  # Change icon to moon
#         else:
#             # Switch to Light Mode
#             self.theme_cls.theme_style = "Light"
#             self.theme_toggle_button.icon = "weather-sunny"  # Change icon to sun

# if __name__ == "__main__":
#     ModuleSearchApp().run()

