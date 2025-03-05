from shiny import App, ui

app_ui = ui.page_fluid(
    # Include Font Awesome from CDN
    ui.tags.head(
        ui.tags.link(
            rel="stylesheet",
            href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"
        )
    ),
    ui.h2("Action Buttons with Icons"),
    ui.card(
        ui.input_action_button("btn1", "Play", icon=ui.tags.i(class_="fa fa-play")),
        ui.input_action_button("btn2", "Download", icon=ui.tags.i(class_="fa fa-download")),
        ui.input_action_button("btn3", "Save", icon=ui.tags.i(class_="fa fa-save")),
        ui.input_action_button("btn4", "GitHub", icon=ui.tags.i(class_="fab fa-github")),
        ui.input_action_button("btn5", "Calendar", icon=ui.tags.i(class_="far fa-calendar")),
        ui.input_action_button("btn6", "Alert", icon=ui.tags.i(class_="fa fa-exclamation-triangle")),
        ui.input_action_button("btn7", "Heart", icon=ui.tags.i(class_="fa fa-heart", style="color: red;")),
        # Icons can also be styled with additional CSS properties
        ui.input_action_button(
            "btn8", 
            "Spinner", 
            icon=ui.tags.i(class_="fa fa-spinner fa-spin")
        ),
        style="display: flex; gap: 10px; flex-wrap: wrap;"
    )
)

def server(input, output, session):
    pass

app = App(app_ui, server)
