import tkinter as tk
from tkinter import ttk, messagebox

class CinemaSchedule:
    def __init__(self):
        self.movies = []
        self.halls = []
        self.schedule = []

    def add_movie(self, title, duration, audience_rating):
        self.movies.append({"title": title, "duration": duration, "rating": audience_rating})

    def add_hall(self, name, capacity):
        self.halls.append({"name": name, "capacity": capacity, "available_times": []})

    def optimize_schedule(self):
        self.schedule = []  # Clear the previous schedule
        if not self.movies or not self.halls:
            return "No movies or halls available."

        # Simple greedy algorithm for scheduling
        self.movies.sort(key=lambda x: x["rating"], reverse=True)  # Sort by audience rating

        for hall in self.halls:
            start_time = 9  # Start at 9:00 AM
            for movie in self.movies:
                if start_time + movie["duration"] / 60 <= 23:  # Check if movie fits before 11 PM
                    end_time = start_time + movie["duration"] / 60
                    self.schedule.append({
                        "hall": hall["name"],
                        "movie": movie["title"],
                        "start_time": f"{int(start_time)}:00",
                        "end_time": f"{int(end_time)}:00",
                    })
                    start_time = end_time  # Update start time for the next movie
                else:
                    break
        return "Schedule optimized successfully!"

    def get_schedule(self):
        if not self.schedule:
            return "No schedule available."
        return "\n".join(
            f"Hall: {s['hall']} | Movie: {s['movie']} | {s['start_time']} - {s['end_time']}"
            for s in self.schedule
        )

class CinemaApp:
    def __init__(self, root):
        self.root = root
        self.schedule_manager = CinemaSchedule()
        self.root.title("Cinema Schedule Optimizer")

        # Movie frame
        movie_frame = ttk.LabelFrame(root, text="Add Movie")
        movie_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        ttk.Label(movie_frame, text="Title:").grid(row=0, column=0, padx=5, pady=5)
        self.movie_title = ttk.Entry(movie_frame)
        self.movie_title.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(movie_frame, text="Duration (mins):").grid(row=1, column=0, padx=5, pady=5)
        self.movie_duration = ttk.Entry(movie_frame)
        self.movie_duration.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(movie_frame, text="Rating:").grid(row=2, column=0, padx=5, pady=5)
        self.movie_rating = ttk.Entry(movie_frame)
        self.movie_rating.grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(movie_frame, text="Add Movie", command=self.add_movie).grid(row=3, column=0, columnspan=2, pady=10)

        # Hall frame
        hall_frame = ttk.LabelFrame(root, text="Add Hall")
        hall_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        ttk.Label(hall_frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        self.hall_name = ttk.Entry(hall_frame)
        self.hall_name.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(hall_frame, text="Capacity:").grid(row=1, column=0, padx=5, pady=5)
        self.hall_capacity = ttk.Entry(hall_frame)
        self.hall_capacity.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(hall_frame, text="Add Hall", command=self.add_hall).grid(row=2, column=0, columnspan=2, pady=10)

        # Schedule frame
        schedule_frame = ttk.LabelFrame(root, text="Schedule")
        schedule_frame.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")

        self.schedule_output = tk.Text(schedule_frame, width=50, height=20)
        self.schedule_output.grid(row=0, column=0, padx=5, pady=5)

        ttk.Button(schedule_frame, text="Optimize Schedule", command=self.optimize_schedule).grid(row=1, column=0, pady=10)

    def add_movie(self):
        title = self.movie_title.get()
        duration = self.movie_duration.get()
        rating = self.movie_rating.get()

        if not title or not duration.isdigit() or not rating.isdigit():
            messagebox.showerror("Error", "Please enter valid movie details.")
            return

        self.schedule_manager.add_movie(title, int(duration), int(rating))
        messagebox.showinfo("Success", f"Movie '{title}' added successfully!")
        self.movie_title.delete(0, tk.END)
        self.movie_duration.delete(0, tk.END)
        self.movie_rating.delete(0, tk.END)

    def add_hall(self):
        name = self.hall_name.get()
        capacity = self.hall_capacity.get()

        if not name or not capacity.isdigit():
            messagebox.showerror("Error", "Please enter valid hall details.")
            return

        self.schedule_manager.add_hall(name, int(capacity))
        messagebox.showinfo("Success", f"Hall '{name}' added successfully!")
        self.hall_name.delete(0, tk.END)
        self.hall_capacity.delete(0, tk.END)

    def optimize_schedule(self):
        result = self.schedule_manager.optimize_schedule()
        self.schedule_output.delete(1.0, tk.END)
        self.schedule_output.insert(tk.END, self.schedule_manager.get_schedule())
        messagebox.showinfo("Info", result)

if __name__ == "__main__":
    root = tk.Tk()
    app = CinemaApp(root)
    root.mainloop()
