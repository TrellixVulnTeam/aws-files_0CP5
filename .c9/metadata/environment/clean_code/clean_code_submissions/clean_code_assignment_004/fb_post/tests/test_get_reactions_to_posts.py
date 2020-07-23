{"filter":false,"title":"test_get_reactions_to_posts.py","tooltip":"/clean_code/clean_code_submissions/clean_code_assignment_004/fb_post/tests/test_get_reactions_to_posts.py","undoManager":{"mark":45,"position":45,"stack":[[{"start":{"row":0,"column":0},"end":{"row":31,"column":0},"action":"insert","lines":["@pytest.mark.django_db","class TestGetReactionsToPosts:","    ","    pytest.mark.django_db","    ","    def test_get_reactions_to_post_with_valid_post_id(","        self, user, post, reactpost):","        ","        # Arrange","        post_id = 2","        reactions_list = [{'user_id': 1, 'name': 'Prathap', 'profile_pic': '', 'reaction': 'LOVE'},","                            {'user_id': 3, 'name': 'Rajesh', 'profile_pic': '', 'reaction': 'SAD'}]","                ","        # Act","        list2 = get_reactions_to_post(post_id)","        ","        # Assert","        assert list2 == reactions_list","     ","        ","    def test_get_reactions_to_post_with_invalid_post_id_raise_error(","        self, user, post, reactpost):","        ","        # Arrange","        post_id = 0","        ","        # Act","        with pytest.raises(InvalidPostException):","                get_reactions_to_post(post_id)","","               ",""],"id":1}],[{"start":{"row":30,"column":15},"end":{"row":31,"column":0},"action":"remove","lines":["",""],"id":2},{"start":{"row":30,"column":14},"end":{"row":30,"column":15},"action":"remove","lines":[" "]},{"start":{"row":30,"column":13},"end":{"row":30,"column":14},"action":"remove","lines":[" "]},{"start":{"row":30,"column":12},"end":{"row":30,"column":13},"action":"remove","lines":[" "]},{"start":{"row":30,"column":8},"end":{"row":30,"column":12},"action":"remove","lines":["    "]},{"start":{"row":30,"column":4},"end":{"row":30,"column":8},"action":"remove","lines":["    "]},{"start":{"row":30,"column":0},"end":{"row":30,"column":4},"action":"remove","lines":["    "]},{"start":{"row":29,"column":0},"end":{"row":30,"column":0},"action":"remove","lines":["",""]},{"start":{"row":28,"column":46},"end":{"row":29,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":28,"column":46},"end":{"row":29,"column":0},"action":"insert","lines":["",""],"id":3},{"start":{"row":29,"column":0},"end":{"row":29,"column":16},"action":"insert","lines":["                "]}],[{"start":{"row":29,"column":12},"end":{"row":29,"column":16},"action":"remove","lines":["    "],"id":4},{"start":{"row":29,"column":8},"end":{"row":29,"column":12},"action":"remove","lines":["    "]},{"start":{"row":29,"column":4},"end":{"row":29,"column":8},"action":"remove","lines":["    "]},{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":5},{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["import pytest","from fb_post.utils.get_posts_reacted_by_user import get_posts_reacted_by_user","from fb_post.exceptions import InvalidUserException",""],"id":6}],[{"start":{"row":8,"column":24},"end":{"row":8,"column":25},"action":"remove","lines":["b"],"id":7},{"start":{"row":8,"column":23},"end":{"row":8,"column":24},"action":"remove","lines":["d"]},{"start":{"row":8,"column":22},"end":{"row":8,"column":23},"action":"remove","lines":["_"]},{"start":{"row":8,"column":21},"end":{"row":8,"column":22},"action":"remove","lines":["o"]},{"start":{"row":8,"column":20},"end":{"row":8,"column":21},"action":"remove","lines":["g"]},{"start":{"row":8,"column":19},"end":{"row":8,"column":20},"action":"remove","lines":["n"]},{"start":{"row":8,"column":18},"end":{"row":8,"column":19},"action":"remove","lines":["a"]},{"start":{"row":8,"column":17},"end":{"row":8,"column":18},"action":"remove","lines":["j"]},{"start":{"row":8,"column":16},"end":{"row":8,"column":17},"action":"remove","lines":["d"]},{"start":{"row":8,"column":15},"end":{"row":8,"column":16},"action":"remove","lines":["."]},{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"remove","lines":["k"]},{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"remove","lines":["r"]},{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"remove","lines":["a"]},{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"remove","lines":["m"]},{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"remove","lines":["."]},{"start":{"row":8,"column":9},"end":{"row":8,"column":10},"action":"remove","lines":["t"]},{"start":{"row":8,"column":8},"end":{"row":8,"column":9},"action":"remove","lines":["s"]},{"start":{"row":8,"column":7},"end":{"row":8,"column":8},"action":"remove","lines":["e"]},{"start":{"row":8,"column":6},"end":{"row":8,"column":7},"action":"remove","lines":["t"]},{"start":{"row":8,"column":5},"end":{"row":8,"column":6},"action":"remove","lines":["y"]},{"start":{"row":8,"column":4},"end":{"row":8,"column":5},"action":"remove","lines":["p"]},{"start":{"row":8,"column":0},"end":{"row":8,"column":4},"action":"remove","lines":["    "]},{"start":{"row":7,"column":4},"end":{"row":8,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"remove","lines":["    "],"id":8},{"start":{"row":6,"column":30},"end":{"row":7,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":1,"column":43},"end":{"row":1,"column":44},"action":"remove","lines":["r"],"id":9},{"start":{"row":1,"column":42},"end":{"row":1,"column":43},"action":"remove","lines":["e"]},{"start":{"row":1,"column":41},"end":{"row":1,"column":42},"action":"remove","lines":["s"]},{"start":{"row":1,"column":40},"end":{"row":1,"column":41},"action":"remove","lines":["u"]},{"start":{"row":1,"column":39},"end":{"row":1,"column":40},"action":"remove","lines":["_"]},{"start":{"row":1,"column":38},"end":{"row":1,"column":39},"action":"remove","lines":["y"]},{"start":{"row":1,"column":37},"end":{"row":1,"column":38},"action":"remove","lines":["b"]},{"start":{"row":1,"column":36},"end":{"row":1,"column":37},"action":"remove","lines":["_"]},{"start":{"row":1,"column":35},"end":{"row":1,"column":36},"action":"remove","lines":["d"]},{"start":{"row":1,"column":34},"end":{"row":1,"column":35},"action":"remove","lines":["e"]},{"start":{"row":1,"column":33},"end":{"row":1,"column":34},"action":"remove","lines":["t"]},{"start":{"row":1,"column":32},"end":{"row":1,"column":33},"action":"remove","lines":["c"]},{"start":{"row":1,"column":31},"end":{"row":1,"column":32},"action":"remove","lines":["a"]},{"start":{"row":1,"column":30},"end":{"row":1,"column":31},"action":"remove","lines":["e"]},{"start":{"row":1,"column":29},"end":{"row":1,"column":30},"action":"remove","lines":["r"]},{"start":{"row":1,"column":28},"end":{"row":1,"column":29},"action":"remove","lines":["_"]},{"start":{"row":1,"column":27},"end":{"row":1,"column":28},"action":"remove","lines":["s"]},{"start":{"row":1,"column":26},"end":{"row":1,"column":27},"action":"remove","lines":["t"]},{"start":{"row":1,"column":25},"end":{"row":1,"column":26},"action":"remove","lines":["s"]},{"start":{"row":1,"column":24},"end":{"row":1,"column":25},"action":"remove","lines":["o"]}],[{"start":{"row":1,"column":23},"end":{"row":1,"column":24},"action":"remove","lines":["p"],"id":10}],[{"start":{"row":1,"column":23},"end":{"row":1,"column":24},"action":"insert","lines":["r"],"id":11},{"start":{"row":1,"column":24},"end":{"row":1,"column":25},"action":"insert","lines":["e"]},{"start":{"row":1,"column":25},"end":{"row":1,"column":26},"action":"insert","lines":["a"]}],[{"start":{"row":1,"column":19},"end":{"row":1,"column":26},"action":"remove","lines":["get_rea"],"id":12},{"start":{"row":1,"column":19},"end":{"row":1,"column":40},"action":"insert","lines":["get_reactions_to_post"]}],[{"start":{"row":1,"column":72},"end":{"row":1,"column":73},"action":"remove","lines":["r"],"id":13},{"start":{"row":1,"column":71},"end":{"row":1,"column":72},"action":"remove","lines":["e"]},{"start":{"row":1,"column":70},"end":{"row":1,"column":71},"action":"remove","lines":["s"]},{"start":{"row":1,"column":69},"end":{"row":1,"column":70},"action":"remove","lines":["u"]},{"start":{"row":1,"column":68},"end":{"row":1,"column":69},"action":"remove","lines":["_"]},{"start":{"row":1,"column":67},"end":{"row":1,"column":68},"action":"remove","lines":["y"]},{"start":{"row":1,"column":66},"end":{"row":1,"column":67},"action":"remove","lines":["b"]},{"start":{"row":1,"column":65},"end":{"row":1,"column":66},"action":"remove","lines":["_"]},{"start":{"row":1,"column":64},"end":{"row":1,"column":65},"action":"remove","lines":["d"]},{"start":{"row":1,"column":63},"end":{"row":1,"column":64},"action":"remove","lines":["e"]},{"start":{"row":1,"column":62},"end":{"row":1,"column":63},"action":"remove","lines":["t"]},{"start":{"row":1,"column":61},"end":{"row":1,"column":62},"action":"remove","lines":["c"]},{"start":{"row":1,"column":60},"end":{"row":1,"column":61},"action":"remove","lines":["a"]},{"start":{"row":1,"column":59},"end":{"row":1,"column":60},"action":"remove","lines":["e"]},{"start":{"row":1,"column":58},"end":{"row":1,"column":59},"action":"remove","lines":["r"]},{"start":{"row":1,"column":57},"end":{"row":1,"column":58},"action":"remove","lines":["_"]},{"start":{"row":1,"column":56},"end":{"row":1,"column":57},"action":"remove","lines":["s"]},{"start":{"row":1,"column":55},"end":{"row":1,"column":56},"action":"remove","lines":["t"]},{"start":{"row":1,"column":54},"end":{"row":1,"column":55},"action":"remove","lines":["s"]},{"start":{"row":1,"column":53},"end":{"row":1,"column":54},"action":"remove","lines":["o"]},{"start":{"row":1,"column":52},"end":{"row":1,"column":53},"action":"remove","lines":["p"]}],[{"start":{"row":1,"column":52},"end":{"row":1,"column":53},"action":"insert","lines":["r"],"id":14},{"start":{"row":1,"column":53},"end":{"row":1,"column":54},"action":"insert","lines":["e"]},{"start":{"row":1,"column":54},"end":{"row":1,"column":55},"action":"insert","lines":["a"]}],[{"start":{"row":1,"column":48},"end":{"row":1,"column":55},"action":"remove","lines":["get_rea"],"id":15},{"start":{"row":1,"column":48},"end":{"row":1,"column":69},"action":"insert","lines":["get_reactions_to_post"]}],[{"start":{"row":2,"column":41},"end":{"row":2,"column":42},"action":"remove","lines":["r"],"id":16},{"start":{"row":2,"column":40},"end":{"row":2,"column":41},"action":"remove","lines":["e"]},{"start":{"row":2,"column":39},"end":{"row":2,"column":40},"action":"remove","lines":["s"]},{"start":{"row":2,"column":38},"end":{"row":2,"column":39},"action":"remove","lines":["U"]}],[{"start":{"row":2,"column":38},"end":{"row":2,"column":39},"action":"insert","lines":["P"],"id":17},{"start":{"row":2,"column":39},"end":{"row":2,"column":40},"action":"insert","lines":["o"]}],[{"start":{"row":2,"column":31},"end":{"row":2,"column":49},"action":"remove","lines":["InvalidPoException"],"id":18},{"start":{"row":2,"column":31},"end":{"row":2,"column":51},"action":"insert","lines":["InvalidPostException"]}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"remove","lines":["    "],"id":19}],[{"start":{"row":9,"column":8},"end":{"row":9,"column":12},"action":"insert","lines":["    "],"id":20}],[{"start":{"row":10,"column":4},"end":{"row":10,"column":8},"action":"remove","lines":["    "],"id":21},{"start":{"row":10,"column":0},"end":{"row":10,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":13,"column":78},"end":{"row":13,"column":79},"action":"remove","lines":[" "],"id":22}],[{"start":{"row":13,"column":78},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":23},{"start":{"row":14,"column":0},"end":{"row":14,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":14,"column":8},"end":{"row":14,"column":12},"action":"insert","lines":["    "],"id":24}],[{"start":{"row":14,"column":12},"end":{"row":14,"column":16},"action":"insert","lines":["    "],"id":25}],[{"start":{"row":14,"column":16},"end":{"row":14,"column":20},"action":"insert","lines":["    "],"id":26}],[{"start":{"row":14,"column":20},"end":{"row":14,"column":24},"action":"insert","lines":["    "],"id":27}],[{"start":{"row":14,"column":24},"end":{"row":14,"column":28},"action":"insert","lines":["    "],"id":28}],[{"start":{"row":14,"column":24},"end":{"row":14,"column":28},"action":"remove","lines":["    "],"id":29}],[{"start":{"row":14,"column":24},"end":{"row":14,"column":25},"action":"insert","lines":[" "],"id":30},{"start":{"row":14,"column":25},"end":{"row":14,"column":26},"action":"insert","lines":[" "]},{"start":{"row":14,"column":26},"end":{"row":14,"column":27},"action":"insert","lines":[" "]}],[{"start":{"row":15,"column":24},"end":{"row":15,"column":28},"action":"remove","lines":["    "],"id":31}],[{"start":{"row":15,"column":24},"end":{"row":15,"column":25},"action":"insert","lines":[" "],"id":32},{"start":{"row":15,"column":25},"end":{"row":15,"column":26},"action":"insert","lines":[" "]}],[{"start":{"row":15,"column":77},"end":{"row":15,"column":78},"action":"remove","lines":[" "],"id":33}],[{"start":{"row":15,"column":77},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":34},{"start":{"row":16,"column":0},"end":{"row":16,"column":26},"action":"insert","lines":["                          "]}],[{"start":{"row":16,"column":26},"end":{"row":16,"column":27},"action":"insert","lines":[" "],"id":35}],[{"start":{"row":17,"column":12},"end":{"row":17,"column":16},"action":"remove","lines":["    "],"id":36},{"start":{"row":17,"column":8},"end":{"row":17,"column":12},"action":"remove","lines":["    "]},{"start":{"row":17,"column":4},"end":{"row":17,"column":8},"action":"remove","lines":["    "]},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":20,"column":4},"end":{"row":20,"column":8},"action":"remove","lines":["    "],"id":37},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"remove","lines":["    "],"id":38},{"start":{"row":22,"column":38},"end":{"row":23,"column":1},"action":"remove","lines":[""," "]}],[{"start":{"row":22,"column":38},"end":{"row":23,"column":0},"action":"insert","lines":["",""],"id":39},{"start":{"row":23,"column":0},"end":{"row":23,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":23,"column":4},"end":{"row":23,"column":8},"action":"remove","lines":["    "],"id":40},{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"remove","lines":["    "],"id":41}],[{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"remove","lines":["    "],"id":42}],[{"start":{"row":26,"column":8},"end":{"row":26,"column":12},"action":"insert","lines":["    "],"id":43}],[{"start":{"row":27,"column":4},"end":{"row":27,"column":8},"action":"remove","lines":["    "],"id":44},{"start":{"row":27,"column":0},"end":{"row":27,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":30,"column":4},"end":{"row":30,"column":8},"action":"remove","lines":["    "],"id":45},{"start":{"row":30,"column":0},"end":{"row":30,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":33,"column":12},"end":{"row":33,"column":16},"action":"remove","lines":["    "],"id":46}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":34,"column":0},"end":{"row":34,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1587807615054,"hash":"f2cf886d63c0b6bc2022cd7e2fb7e429cc0eab08"}