$(document).ready(function () {
    $('input[type="checkbox"][name="only_3_js"]').change(
        function () {
            if ($(this).prop('checked')) {
                $('div.media:gt(2)').addClass('hidden');
            } else {
                $('div.media').removeClass('hidden');
            }
        }
    );
});