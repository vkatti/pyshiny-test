from shiny import ui, render, reactive, App

ui = ui.page_navbar(
    ui.nav_panel(
        "Home",
        ui.input_numeric("a", label="First Number", value=1),
        ui.input_numeric("b", label="Second Number", value=2),
        ui.input_action_button("sum", label="Sum", style="color: white; background-color: blue;"),
        ui.output_text("result"),
        value = "home"
        ),
    ui.nav_panel(title="Inwards", value="inwards"),
    ui.nav_panel(title="Indents", value="indents"),
    ui.nav_panel(title="Operations", value="operations"),
    ui.nav_panel(title="Reports", value="reports"),
    ui.nav_panel(title="Settings", value="settings"),
    title = "Hello, World!"
)

def server(input, output, session): 

    def sum(a,b): 
        print(f"sum({a},{b})={a+b}")
        return a + b

    @render.text
    @reactive.event(input.sum)
    def result(): 
        return sum(input.a(), input.b())
    

app = App(ui, server)