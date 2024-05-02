remaining_change = float(input())
change_as_stotinki = int(remaining_change * 100)
coins_taken = 0

while change_as_stotinki > 0:
    if change_as_stotinki >= 200:
        change_as_stotinki -= 200
    elif change_as_stotinki >= 100:
        change_as_stotinki -= 100
    elif change_as_stotinki >= 50:
        change_as_stotinki -= 50
    elif change_as_stotinki >= 20:
        change_as_stotinki -= 20
    elif change_as_stotinki >= 10:
        change_as_stotinki -= 10
    elif change_as_stotinki >= 5:
        change_as_stotinki -= 5
    elif change_as_stotinki >= 2:
        change_as_stotinki -= 2
    elif change_as_stotinki >= 1:
        change_as_stotinki -= 1
    coins_taken += 1

print(coins_taken)
