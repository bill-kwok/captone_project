import streamlit as st
import pandas as pd

def num_to_card(num):
  suit_dict = {0:'Spade', 1:'Heart', 2:'Club', 3:'Diamond'}
  rank_dict = {1:'A', 11:'J', 12:'Q', 13:'K'}
  suit = suit_dict[num // 13]
  rank = num % 13 + 1
  if (rank == 1) | (rank > 10):
    rank = rank_dict[rank]
  return suit + ' ' + str(rank)

df = pd.read_csv("data_for_first_two_cards.csv")
deck = [num_to_card(i) for i in range(52)]

def reset_game():
  remaining_deck = deck.copy()
  my_cards, community = set({}), set({})
  flop, turn, river = '', '', ''
  return remaining_deck, my_cards, community, flop, turn, river
    
st.header("Welcome for using this calculator for Texas Hold'em Poker!")
st.text("")

with st.sidebar:
  table = st.checkbox("Table")
  dp = st.slider("Number of decimal places", 1, 6, 2)
  st.title("")
  st.title("")
  bar = st.checkbox("Bar chart")
  bar_size = st.slider("Size of bar chart", 1, 10, 5)
  st.title("")
  st.title("")
  pie = st.checkbox("Pie chart")
  pie_size = st.slider("Size of pie chart", 1, 10, 5)

col1, col2 = st.columns([1,3])

with col1:
  remaining_deck, my_cards, community, flop, turn, river = reset_game()
  game = st.button("Start a new game")  

  selection1 = st.multiselect("Which 2 cards have you got:", remaining_deck)
  enter1 = st.checkbox("Confirm the 2 cards")
  if enter1:
    my_cards.update(set(selection1))
  st.write(my_cards)
      
  selection2 = st.multiselect("The flop: first 3 community cards", remaining_deck)
  enter2 = st.checkbox("Confirm the first 3 community cards")
  if enter2:
    flop = selection2.copy()
  st.write(flop)
  
  selection3 = st.selectbox("The turn: 4th community card", remaining_deck)
  enter3 = st.checkbox("Confirm the 4th community card")
  if enter3:
    turn = selection3
  st.write(turn)
  
  selection4 = st.selectbox("The river: 5th community card", remaining_deck)
  enter4 = st.checkbox("Confirm the 5th community card")
  if enter4:
    river = selection4
  st.write(river)
  
  if game:
    enter1, enter2, enter3, enter4 = False, False, False, False      
    
with col2:
  if table:
    df
  

