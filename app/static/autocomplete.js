$(document).ready(function() {
    $("#search-box").on("input", function() {
        let query = $(this).val();
        if (query.length > 0) {
            $.ajax({
                url: `/autocomplete/`,
                type: "GET",
                data: { query: query },
                success: function(data) {
                    console.log(data);
                    suggestions = data.suggestions;
                    $("#suggestions").empty();
                    suggestions.forEach(item => {
                        console.log(item);
                        $("#suggestions").append(`<a href="#" class="list-group-item list-group-item-action">${item}</a>`);
                        $("#suggestions").on("click", ".list-group-item", function() {
                            $("#search-box").val($(this).text());
                            $("#suggestions").empty();
                        });
                    });
                }
            });
        } else {
            $("#suggestions").empty();
        }
    });
});
