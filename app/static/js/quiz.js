$(document).ready(function() {
    $.ajax({
        type: "GET",
        url: "/Quizzes/getQuestions",
        success: function(result) {

            $('#question_1').text(result.question_1)
            $('#answer1_string_1').text(result.answer1_string_1)
            $('#answer2_string_1').text(result.answer2_string_1)
            $('#answer3_string_1').text(result.answer3_string_1)
            $('#answer4_string_1').text(result.answer4_string_1)
            $('#QID1').text(result.QID1)

            $('#question_2').text(result.question_2)
            $('#answer1_string_2').text(result.answer1_string_2)
            $('#answer2_string_2').text(result.answer2_string_2)
            $('#answer3_string_2').text(result.answer3_string_2)
            $('#answer4_string_2').text(result.answer4_string_2)
            $('#QID2').text(result.QID2)

            $('#question_3').text(result.question_3)
            $('#answer1_string_3').text(result.answer1_string_3)
            $('#answer2_string_3').text(result.answer2_string_3)
            $('#answer3_string_3').text(result.answer3_string_3)
            $('#answer4_string_3').text(result.answer4_string_3)
            $('#QID3').text(result.QID3)

            $('#question_4').text(result.question_4)
            $('#answer1_string_4').text(result.answer1_string_4)
            $('#answer2_string_4').text(result.answer2_string_4)
            $('#answer3_string_4').text(result.answer3_string_4)
            $('#answer4_string_4').text(result.answer4_string_4)
            $('#QID4').text(result.QID4)

            $('#question_5').text(result.question_5)
            $('#answer1_string_5').text(result.answer1_string_5)
            $('#answer2_string_5').text(result.answer2_string_5)
            $('#answer3_string_5').text(result.answer3_string_5)
            $('#answer4_string_5').text(result.answer4_string_5)
            $('#QID5').text(result.QID5)
        }
    });
    $('#calculate').click(function() {
        item = {}
        item["QID1"] = $('#QID1').text()
        item["QID2"] = $('#QID2').text()
        item["QID3"] = $('#QID3').text()
        item["QID4"] = $('#QID4').text()
        item["QID5"] = $('#QID5').text()
        item["answer_1"] = $('input:radio[name=answer_1]:checked').val();
        item["answer_2"] = $('input:radio[name=answer_2]:checked').val();
        item["answer_3"] = $('input:radio[name=answer_3]:checked').val();
        item["answer_4"] = $('input:radio[name=answer_4]:checked').val();
        item["answer_5"] = $('input:radio[name=answer_5]:checked').val();
        if (item["answer_1"] === undefined || item["answer_2"] === undefined || item["answer_3"] === undefined || item["answer_4"] === undefined || item["answer_5"] === undefined) {
            alert('Please answer all questions!');
        } else {
            alert('Submitted!!');
            $.ajax({
                type: "POST",
                url: "/Quizzes/Evaluate",
                data: JSON.stringify(item),
                contentType: 'application/json;charset=UTF-8',
                success: function(result) {
                    $('#Mark').text(result.Score)
                    $('#Correct').text(result.Correct)
                }
            });
        }
    });
    $('#reset').click(function() {
        $('input:radio').prop('checked', false)
        $('#Mark').text("Your score:")
        $('#Correct').text("Questions answered correct:")
    });
});