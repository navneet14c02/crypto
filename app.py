import flet as ft

def main(page: ft.Page):
    page.title = "Taxi App Prototype"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_width = 380
    page.window_height = 700
    page.scroll = "auto"

    # UI Elements
    pickup = ft.TextField(label="Pickup Location", prefix_icon=ft.icons.LOCATION_ON, border_color="yellow700")
    drop = ft.TextField(label="Where to?", prefix_icon=ft.icons.STREETVIEW, border_color="black")
    
    # Ride Selection
    ride_type = ft.RadioGroup(content=ft.Row([
        ft.Radio(value="Bike", label="Bike (₹5/km)"),
        ft.Radio(value="Car", label="Car (₹12/km)"),
    ]))

    result_text = ft.Text("", size=18, weight="bold", color="green")

    def book_ride(e):
        if not pickup.value or not drop.value or not ride_type.value:
            result_text.value = "Please fill all details!"
            result_text.color = "red"
        else:
            # Simple Logic: Maan lete hain distance 10km hai
            distance = 10 
            rate = 5 if ride_type.value == "Bike" else 12
            fare = distance * rate
            result_text.value = f"Ride Booked! Total Fare: ₹{fare}"
            result_text.color = "green"
        page.update()

    # Layout
    page.add(
        ft.Container(
            content=ft.Text("MY TAXI APP", size=30, weight="bold", color="black"),
            bgcolor="yellow700",
            padding=20,
            alignment=ft.alignment.center,
        ),
        ft.Column([
            ft.Text("Book your ride now", size=20, weight="w500"),
            pickup,
            drop,
            ft.Text("Select Vehicle:"),
            ride_type,
            ft.ElevatedButton(
                "BOOK NOW", 
                on_pressed=book_ride,
                style=ft.ButtonStyle(
                    color="white",
                    bgcolor="black",
                    shape=ft.RoundedRectangleBorder(radius=10),
                ),
                width=400,
                height=50
            ),
            ft.Divider(),
            result_text
        ], spacing=20, padding=20)
    )

ft.app(target=main)
