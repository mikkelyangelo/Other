$(window).on('load', function () {

    let currentDate = new Date();
    let maxDateDay = currentDate.toISOString().split('T')[0]; // формат YYYY-MM-DD
    let maxDateMonth = maxDateDay.slice(0, 7); // формат YYYY-MM
    let minDateDay = "2020-01-01"; // формат YYYY-MM-DD для типа date
    let minDateMonth = "2020-01"; // формат YYYY-MM для типа month

    $('input[type="date"]').each(function () {
        $(this).attr('max', maxDateDay);
        $(this).attr('min', minDateDay);
    });

    $('input[type="month"]').each(function () {
        $(this).attr('max', maxDateMonth);
        $(this).attr('min', minDateMonth);
    });
});

$(document).ready(function () {
    var sqlResults = $('.sql-results');
    if (sqlResults.length) {
        sqlResults[0].scrollIntoView({ behavior: "smooth" });
    }
});

$(document).ready(function () {
    $('#search').on('input', function () {
        var searchQuery = $(this).val().toLowerCase();
        var firstRow = true;

        $('tbody tr').each(function () {
            var medName = $(this).find('td:first').text().toLowerCase();

            if (medName.includes(searchQuery)) {
                $(this).show();

                if (firstRow) {
                    $(this).find('td').css('border-top', 'none');
                    firstRow = false;
                } else {
                    $(this).find('td').css('border-top', '');
                }
            } else {
                $(this).hide();
            }
        });
    });
});