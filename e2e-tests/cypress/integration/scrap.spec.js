describe("Let's start scrapping jobs", () => {
  it("Visit indeed!", () => {
    cy.visit("https://indeed.com");
    cy.get("#text-input-what").should("be.visible");
    cy.get("#text-input-what").type("Test Engineer");
    cy.get("#text-input-where").type("Singapur, PR");
    cy.get("#jobsearch").contains("Find jobs").click();
    cy.get(".resultsTop").contains("Upload your resume").should("be.visible");
    let jobs = [];
    cy.get("#resultsCol")
      .get(".jcs-JobTitle")
      .then(function ($elem) {
        jobs.push($elem.text());
      });
    cy.log(jobs);
  });
});
