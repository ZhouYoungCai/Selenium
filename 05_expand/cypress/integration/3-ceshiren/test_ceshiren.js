describe('搜索功能',()=>{
    beforeEach(()=>{
        //打开网页
        cy.visit("https://ceshiren.com/")
    })
    it("搜索功能正向测试", ()=>{
        cy.get("#search-button").click()
        cy.get("#search-term").type("测试开发")
        cy.get("#search-term").type("{enter}")
        //断言
        cy.get("[data-topic-id='10980']").should('contain', "测试")

    })







})