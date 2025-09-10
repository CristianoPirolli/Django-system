from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty, ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class AnimalListScreen(Screen):
    def on_pre_enter(self):
        animal_list = self.ids.animal_list
        animal_list.clear_widgets()
        app = App.get_running_app()
        for animal in app.animals:
            box = BoxLayout(size_hint_y=None, height='40dp')
            btn = Button(
                text=f"{animal['brinco']} - {animal['sexo']} - {animal['idade']}",
                size_hint_x=0.7
            )
            btn.bind(on_release=lambda btn, a=animal: self.select_animal(a))
            rm = Button(text='Remover', size_hint_x=0.3)
            rm.bind(on_release=lambda btn, a=animal: self.remove_animal(a))
            box.add_widget(btn)
            box.add_widget(rm)
            animal_list.add_widget(box)

    def select_animal(self, animal):
        app = App.get_running_app()
        app.current_animal = animal
        self.manager.current = 'vaccines'

    def remove_animal(self, animal):
        app = App.get_running_app()
        if animal in app.animals:
            app.animals.remove(animal)
        self.on_pre_enter()


class AddAnimalScreen(Screen):
    sexo_input = ObjectProperty(None)
    idade_input = ObjectProperty(None)
    brinco_input = ObjectProperty(None)
    brinco_mae_input = ObjectProperty(None)

    def save_animal(self):
        app = App.get_running_app()
        animal = {
            'sexo': self.sexo_input.text,
            'idade': self.idade_input.text,
            'brinco': self.brinco_input.text,
            'brinco_mae': self.brinco_mae_input.text,
            'vacinas': []
        }
        app.animals.append(animal)
        self.sexo_input.text = ''
        self.idade_input.text = ''
        self.brinco_input.text = ''
        self.brinco_mae_input.text = ''
        self.manager.current = 'animals'


class VaccineListScreen(Screen):
    def on_pre_enter(self):
        vaccine_list = self.ids.vaccine_list
        vaccine_list.clear_widgets()
        app = App.get_running_app()
        animal = app.current_animal
        if not animal:
            return
        for vac in animal['vacinas']:
            box = BoxLayout(size_hint_y=None, height='40dp')
            label_text = f"{vac['nome']} - {vac['data']}"
            if vac['segunda_dose']:
                label_text += f" / 2ª: {vac['data_segunda_dose']}"
            box.add_widget(Label(text=label_text))
            rm = Button(text='Remover', size_hint_x=0.3)
            rm.bind(on_release=lambda btn, v=vac: self.remove_vaccine(v))
            box.add_widget(rm)
            vaccine_list.add_widget(box)

    def remove_vaccine(self, vaccine):
        app = App.get_running_app()
        animal = app.current_animal
        if animal and vaccine in animal['vacinas']:
            animal['vacinas'].remove(vaccine)
        self.on_pre_enter()


class AddVaccineScreen(Screen):
    vaccine_name = ObjectProperty(None)
    application_date = ObjectProperty(None)
    second_dose = ObjectProperty(None)
    second_date = ObjectProperty(None)

    def save_vaccine(self):
        app = App.get_running_app()
        animal = app.current_animal
        if not animal:
            return
        vaccine = {
            'nome': self.vaccine_name.text,
            'data': self.application_date.text,
            'segunda_dose': self.second_dose.active,
            'data_segunda_dose': self.second_date.text if self.second_dose.active else ''
        }
        animal['vacinas'].append(vaccine)
        self.vaccine_name.text = ''
        self.application_date.text = ''
        self.second_dose.active = False
        self.second_date.text = ''
        self.manager.current = 'vaccines'


class RootWidget(ScreenManager):
    pass


class CattleApp(App):
    animals = ListProperty([])
    current_animal = ObjectProperty(None)

    def build(self):
        return Builder.load_file('main.kv')


if __name__ == '__main__':
    CattleApp().run()
