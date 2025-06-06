class Tool:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.available = True
        self.rented_by = '' 

    def rent(self, customer_name):
        if self.available:
            print(f"The tool {self.name} has been rented by {customer_name}")
            self.available = False
            self.rented_by = customer_name
            return True
        else:
            print(f"The tool {self.name} is not available for rent")
            return False
    
    def return_tool(self):
        if not self.available:
            print(f"The tool {self.name} has been returned by {self.rented_by}")
            self.available = True
            self.rented_by = ''
        else:
            print(f"The tool {self.name} was never rented!!!")
    
    def display_info(self):
        if self.available:
            print(f"The tool {self.name} is available.")
        else:
            print(f"The tool {self.name} was rented by {self.rented_by}")


class Customer:
    def __init__(self, name):
        self.name = name
        self.rented_tools = []

    def rent_tool(self, tool):
        if tool.rent(self.name):
            self.rented_tools.append(tool.name)

    def return_tool(self, tool):
        if tool.name in self.rented_tools:
            tool.return_tool()
            self.rented_tools.remove(tool.name)

    def show_rented_tools(self):
        print(f"{self.name} currently has: {self.rented_tools}")


# Simulation
customer1 = Customer("Mike")
customer2 = Customer("Jane")

tool1 = Tool("Drill", "Power")
tool2 = Tool("Hammer", "Hand")

customer1.rent_tool(tool1)
customer1.rent_tool(tool2)

customer2.rent_tool(tool1)  # Should say not available

customer1.return_tool(tool1)
customer2.rent_tool(tool1)  # Now it's available

customer1.show_rented_tools()
customer2.show_rented_tools()
