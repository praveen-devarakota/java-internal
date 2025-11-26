const fileMap = {
    1: "Java-week-1.docx",
    2: "Java-week-2.docx",
    3: "Java-week-3.docx",
    4: "Java week-4.docx",
    5: "Java week-5.docx",
    6: "JAVA-WEEK-6.docx",
    7: "Java-week-7.docx",
    8: "JAVA-WEEK-8.docx",
    9: "JAVA-WEEK-9.docx",
    10: "JAVA-WEEK-10.docx",
    11: "JAVA-WEEK-11.docx",
    12: "JAVA-WEEK-12.docx"
};

function loadWeek(week) {
    document.getElementById("week-title").innerText = `Week ${week} Content`;

    document.getElementById("frame").src = `converted/week${week}.html`;

    document.getElementById("downloadLink").href = `docs/${fileMap[week]}`;
}
