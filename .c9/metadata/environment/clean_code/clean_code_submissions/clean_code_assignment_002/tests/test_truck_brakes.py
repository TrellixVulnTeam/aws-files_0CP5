{"filter":false,"title":"test_truck_brakes.py","tooltip":"/clean_code/clean_code_submissions/clean_code_assignment_002/tests/test_truck_brakes.py","undoManager":{"mark":18,"position":18,"stack":[[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["f"],"id":1},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":["r"]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["o"]},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":["m"]}],[{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"insert","lines":[" "],"id":2},{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"insert","lines":["t"]},{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"insert","lines":["r"]},{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"insert","lines":["u"]},{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"insert","lines":["c"]},{"start":{"row":0,"column":9},"end":{"row":0,"column":10},"action":"insert","lines":["k"]}],[{"start":{"row":0,"column":10},"end":{"row":0,"column":11},"action":"insert","lines":[" "],"id":3},{"start":{"row":0,"column":11},"end":{"row":0,"column":12},"action":"insert","lines":["i"]},{"start":{"row":0,"column":12},"end":{"row":0,"column":13},"action":"insert","lines":["m"]},{"start":{"row":0,"column":13},"end":{"row":0,"column":14},"action":"insert","lines":["p"]},{"start":{"row":0,"column":14},"end":{"row":0,"column":15},"action":"insert","lines":["o"]},{"start":{"row":0,"column":15},"end":{"row":0,"column":16},"action":"insert","lines":["r"]},{"start":{"row":0,"column":16},"end":{"row":0,"column":17},"action":"insert","lines":["t"]}],[{"start":{"row":0,"column":17},"end":{"row":0,"column":18},"action":"insert","lines":[" "],"id":4},{"start":{"row":0,"column":18},"end":{"row":0,"column":19},"action":"insert","lines":["T"]},{"start":{"row":0,"column":19},"end":{"row":0,"column":20},"action":"insert","lines":["r"]},{"start":{"row":0,"column":20},"end":{"row":0,"column":21},"action":"insert","lines":["u"]},{"start":{"row":0,"column":21},"end":{"row":0,"column":22},"action":"insert","lines":["c"]},{"start":{"row":0,"column":22},"end":{"row":0,"column":23},"action":"insert","lines":["k"]}],[{"start":{"row":0,"column":23},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":5},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""]},{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["",""],"id":6}],[{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":7}],[{"start":{"row":3,"column":0},"end":{"row":46,"column":0},"action":"insert","lines":["# case-11","def test_apply_brakes_when_truck_current_speed_is_less_than_tyre_friction():","","    # Arrange","    truck = Truck(","        color='Blue',","        max_speed=5,","        acceleration=3,","        tyre_friction=4,","        max_cargo_weight=1","    )","    truck.start_engine()","    truck.accelerate()","","    # Act","    truck.apply_brakes()","    current_speed_value = 0","","    # Assert","    assert truck.current_speed == current_speed_value","","","# case-12","def test_apply_brakes_when_truck_current_speed_is_more_than_tyre_friction():","","    # Arrange","    truck = Truck(","        color='Blue',","        max_speed=5,","        acceleration=4,","        tyre_friction=3,","        max_cargo_weight=1","    )","    truck.start_engine()","    truck.accelerate()","","    # Act","    truck.apply_brakes()","    current_speed_value = 1","","    # Assert","    assert truck.current_speed == current_speed_value","",""],"id":8}],[{"start":{"row":45,"column":0},"end":{"row":46,"column":0},"action":"remove","lines":["",""],"id":9}],[{"start":{"row":8,"column":18},"end":{"row":8,"column":19},"action":"remove","lines":["e"],"id":10},{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"remove","lines":["u"]},{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"remove","lines":["l"]},{"start":{"row":8,"column":15},"end":{"row":8,"column":16},"action":"remove","lines":["B"]}],[{"start":{"row":8,"column":15},"end":{"row":8,"column":16},"action":"insert","lines":["L"],"id":11},{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"insert","lines":["I"]}],[{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"remove","lines":["I"],"id":12}],[{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"insert","lines":["i"],"id":13},{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"insert","lines":["g"]},{"start":{"row":8,"column":18},"end":{"row":8,"column":19},"action":"insert","lines":["h"]},{"start":{"row":8,"column":19},"end":{"row":8,"column":20},"action":"insert","lines":["t"]},{"start":{"row":8,"column":20},"end":{"row":8,"column":21},"action":"insert","lines":["C"]},{"start":{"row":8,"column":21},"end":{"row":8,"column":22},"action":"insert","lines":["y"]},{"start":{"row":8,"column":22},"end":{"row":8,"column":23},"action":"insert","lines":["a"]}],[{"start":{"row":8,"column":23},"end":{"row":8,"column":24},"action":"insert","lines":["n"],"id":14}],[{"start":{"row":30,"column":18},"end":{"row":30,"column":19},"action":"remove","lines":["e"],"id":15},{"start":{"row":30,"column":17},"end":{"row":30,"column":18},"action":"remove","lines":["u"]},{"start":{"row":30,"column":16},"end":{"row":30,"column":17},"action":"remove","lines":["l"]},{"start":{"row":30,"column":15},"end":{"row":30,"column":16},"action":"remove","lines":["B"]}],[{"start":{"row":30,"column":15},"end":{"row":30,"column":16},"action":"insert","lines":["L"],"id":16},{"start":{"row":30,"column":16},"end":{"row":30,"column":17},"action":"insert","lines":["I"]}],[{"start":{"row":30,"column":16},"end":{"row":30,"column":17},"action":"remove","lines":["I"],"id":17}],[{"start":{"row":30,"column":16},"end":{"row":30,"column":17},"action":"insert","lines":["i"],"id":18},{"start":{"row":30,"column":17},"end":{"row":30,"column":18},"action":"insert","lines":["g"]},{"start":{"row":30,"column":18},"end":{"row":30,"column":19},"action":"insert","lines":["h"]},{"start":{"row":30,"column":19},"end":{"row":30,"column":20},"action":"insert","lines":["t"]},{"start":{"row":30,"column":20},"end":{"row":30,"column":21},"action":"insert","lines":["G"]}],[{"start":{"row":30,"column":21},"end":{"row":30,"column":22},"action":"insert","lines":["r"],"id":19},{"start":{"row":30,"column":22},"end":{"row":30,"column":23},"action":"insert","lines":["e"]},{"start":{"row":30,"column":23},"end":{"row":30,"column":24},"action":"insert","lines":["e"]},{"start":{"row":30,"column":24},"end":{"row":30,"column":25},"action":"insert","lines":["n"]}]]},"ace":{"folds":[],"scrolltop":208,"scrollleft":0,"selection":{"start":{"row":30,"column":25},"end":{"row":30,"column":25},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":9,"state":"start","mode":"ace/mode/python"}},"timestamp":1587546283127,"hash":"f7a95dc825ddcec332b097b1246d6f1f753f0b57"}