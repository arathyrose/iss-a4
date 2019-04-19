$(document).ready(function() {
    $('#next_plain_text').click(function() {
        $.ajax({
            type: "GET",
            url: "/Experiment/next_plain_text",
            success: function(result) {
                $('#plainarea').val(result.plainarea);
                //console.log(result);
                //console.log(result.plainarea);
            }
        });
    });
    $('#next_key').click(function() {
        $.ajax({
            type: "GET",
            url: "/Experiment/next_key",
            success: function(result) {
                $('#key').val(result.key);
                //console.log(result);
                //console.log(result.key);
            }
        });
    });
    $('#Next_Encryption').click(function() {
        $.ajax({
            type: "GET",
            url: "/Experiment/Next_Encryption",
            success: function(result) {
                $('#current_encryption').val(result.current_encryption);
                //console.log(result);
                //console.log(result.current_encryption);
            }
        });
    });
    $('#Encrypt1').click(function() {
        item = {}
        item["key"] = $('#key').val();
        item["plainarea"] = $('#plainarea').val();
        item["current_encryption"] = $('#current_encryption').val()
            //console.log(item)
        $.ajax({
            type: "POST",
            url: "/Experiment/Encrypt1",
            data: JSON.stringify(item),
            contentType: 'application/json;charset=UTF-8',
            success: function(result) {
                $('#cipherarea').val(result.ciphertext);
                //console.log(result);
                //console.log(result.ciphertext);
            }
        });
    });
    $('#gen_all_pairs').click(function() {
        item = {}
        item["user_key"] = $('#user_key').val();
        item["current_encryption"] = $('#current_encryption').val()
        if (user_key == "") {
            alert("Enter some binary string as the user key");
            return;
        }
        //console.log(item)
        $.ajax({
            type: "POST",
            url: "/Experiment/gen_all_pairs",
            data: JSON.stringify(item),
            contentType: 'application/json;charset=UTF-8',
            success: function(result) {
                if (result.message == "") {
                    $('#encryption_set').val(result.encryption_set);
                    //console.log(result);
                    //console.log(result.encryption_set);
                } else {
                    alert(result.message);
                    $('#encryption_set').val("");
                    $('#user_key').val("01010100");
                }
            }
        });
    });
    $('#checkAnswer').click(function() {
        item = {}
        item["yesno"] = $('#yesno').val();
        item["user_key"] = $('#user_key').val();
        item["m1"] = $('#m1').val();
        item["m2"] = $('#m2').val();
        item["current_encryption"] = $('#current_encryption').val()
            //console.log(item)
        $.ajax({
            type: "POST",
            url: "/Experiment/checkAnswer",
            data: JSON.stringify(item),
            contentType: 'application/json;charset=UTF-8',
            success: function(result) {
                if (result.message == "") {
                    $('#results').val(result.results);
                    //console.log(result);
                    //console.log(result.results);
                } else {
                    alert(result.message);
                    if (result.messageType == "user_key") $('#user_key').val("01010100");
                    if (result.messageType == "m1") $('#m1').val("");
                    if (result.messageType == "m2") $('#m2').val("");
                    if (result.messageType == "m12") {
                        $('#m1').val("");
                        $('#m2').val("");
                    }
                }
            }
        });
    });
    $('#simulation_key_generator').click(function() {
        item = {}
        item["simulation_plainarea"] = $('#simulation_plainarea').val();
        item["simulation_cipherarea"] = $('#simulation_cipherarea').val();
        //console.log(item)
        $.ajax({
            type: "POST",
            url: "/Experiment/simulation_key_generator",
            data: JSON.stringify(item),
            contentType: 'application/json;charset=UTF-8',
            success: function(result) {
                if (result.message == "") {
                    $('#simulation_key').val(result.simulation_key);
                    //console.log(result);
                    //console.log(result.simulation_key);
                } else {
                    alert(result.message);
                    if (result.messageType == "plaintext") $('#simulation_plainarea').val("");
                    if (result.messageType == "ciphertext") $('#simulation_cipherarea').val("");
                }
            }
        });
    });

    $('#simulation_encrypt').click(function() {
        item = {}
        item["simulation_plainarea"] = $('#simulation_plainarea').val();
        item["simulation_key"] = $('#simulation_key').val();
        //console.log(item)
        $.ajax({
            type: "POST",
            url: "/Experiment/simulation_encrypt",
            data: JSON.stringify(item),
            contentType: 'application/json;charset=UTF-8',
            success: function(result) {
                if (result.message == "") {
                    $('#simulation_cipherarea').val(result.simulation_cipherarea);
                    //console.log(result);
                    //console.log(result.simulation_cipherarea);
                } else {
                    alert(result.message);
                    if (result.messageType == "plaintext") $('#simulation_plainarea').val("");
                    if (result.messageType == "key") $('#simulation_key').val("");
                }
            }
        });
    });

    $('#simulation_decrypt').click(function() {
        item = {}
        item["simulation_cipherarea"] = $('#simulation_cipherarea').val();
        item["simulation_key"] = $('#simulation_key').val();
        //console.log(item)
        $.ajax({
            type: "POST",
            url: "/Experiment/simulation_decrypt",
            data: JSON.stringify(item),
            contentType: 'application/json;charset=UTF-8',
            success: function(result) {
                if (result.message == "") {
                    $('#simulation_plainarea').val(result.simulation_plainarea);
                    //console.log(result);
                    //console.log(result.simulation_plainarea);
                } else {
                    alert(result.message);
                    if (result.messageType == "ciphertext") $('#simulation_cipherarea').val("");
                    if (result.messageType == "key") $('#simulation_key').val("");
                }
            }
        });
    });
});