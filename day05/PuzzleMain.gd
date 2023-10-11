extends Node

func _ready() -> void:
	var input: String = read_input("res://puzzle_input.tres")
	var data: Array = format(input)
	var instructions: Array = format_instructions(data[1].duplicate())
	print("0: ", data[0])
	
	var piles_final_1: Array = follow_instructions(data[0].duplicate(), instructions.duplicate(), "a")
	print("1:", data[0])
	var piles_final_2: Array = follow_instructions(data[0].duplicate(), instructions.duplicate(), "b")
	print("2.", data[0])
	
	var result_a: String = get_results(piles_final_1)
	print(result_a)
	var result_b: String = get_results(piles_final_2)
	print(result_b)


func read_input(input_file_location) -> String:
	var file: File = File.new()
	file.open("res://puzzle_input.tres", File.READ)
	var content: String = file.get_as_text()
	file.close()
	return content


func format(input) -> Array:
	var lines: Array = input.split("\n")
	lines.remove(lines.size()-1)

	#-----Isolate Stacks & Instructions-----#
	var stacks: Array = []
	var instructions: Array = []
	var batch = []
	for line in lines:
		if line.length() < 1:
			stacks.append_array(batch)
			batch.clear()
		batch.append(line)
	instructions.append_array(batch)
	instructions.remove(0)

	var stacks_f: Array = []
	for line in stacks:
		var l = line
		l = l.replace("\t", "....")
		l = l.replace("[", ".")
		l = l.replace("]", ".")
		l = l.replace(" ", ".")
		stacks_f.append(l)
	stacks_f.pop_back()

	#-----Stack Height-----#
	var stack_height: int = stacks.size()

	#-----Stack Width-----#
	var stack_width: int = 0
	for line in lines:
		if "1".is_subsequence_of(line):
			stack_width = line.replace(" ", "").length()
			break

	#-----Crate Positions-----#
	var piles: Array = []
	for i in range(stack_width):
		var emptylist: Array = []
		piles.append(emptylist)
	var pile_nr: int = 0
	for line in stacks_f:
		var count: int = 0
		var content = []
		for i in range(line.length()):
			content.append(line[i])
			count += 1
			if count == 4 or i == line.length()-1:
				for c in content:
					if c != ".":
						piles[pile_nr].append(c)
				content.clear()
				count = 0
				pile_nr += 1
		pile_nr = 0

	var data: Array = [piles, instructions]
	return data


func format_instructions(instructions) -> Array:
	var instructions_new: Array = []
	for line in instructions:
		var p: Array = []
		p.append_array(line.split(" "))
		p.pop_at(0)
		p.pop_at(1)
		p.pop_at(2)
		instructions_new.append(p)
	return instructions_new


func follow_instructions(piles, instructions, puzzle) -> Array:
	var piles_final: Array = []
	piles_final.append_array(piles.duplicate())
	for inst in instructions:
		var piles_new = []
		if puzzle == "a":
			piles_new.append_array(move_crates(piles_final, inst[0], inst[1], inst[2]))
		elif puzzle == "b":
			piles_new.append_array(move_crates_2(piles_final, inst[0], inst[1], inst[2]))
		piles_final.clear()
		piles_final.append_array(piles_new)
	return piles_final


func move_crates(piles, amount, from, to) -> Array:
	var piles_new_x: Array
	piles_new_x.append_array(piles.duplicate())
	for i in range(int(amount)):
		var crate = piles_new_x[int(from)-1].pop_front()
		piles_new_x[int(to)-1].push_front(crate)
	return piles_new_x


func move_crates_2(piles, amount, from, to) -> Array:
	var piles_new_y: Array
	piles_new_y.append_array(piles.duplicate())
	var temp_array: Array = []
	for i in range(int(amount)):
		var crate_a = piles_new_y[int(from)-1].pop_front()
		temp_array.append(crate_a)
	for i in range(temp_array.size()):
		var crate_b = temp_array.pop_back()
		piles_new_y[int(to)-1].push_front(crate_b)
	return piles_new_y


func get_results(piles) -> String:
	var result: String = ""
	for pile in piles:
		result += pile[0]
	return result
