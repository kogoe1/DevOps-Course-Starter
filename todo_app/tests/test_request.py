
from todo_app.tests.test_response import MockedResponse

class MockedRequests:

    trello_boards = {"id":"5fb51906cc7d395b1b145b0e","name":"TO DO List",
                        "lists":[   {"id":"5fb51906cc7d395b1b145b0f","name":"To Do","closed":'false',"pos":16384,"softLimit":'null',"idBoard":"5fb51906cc7d395b1b145b0e","subscribed":'false'},
                                    {"id":"5fb51906cc7d395b1b145b10","name":"Doing","closed":'false',"pos":32768,"softLimit":'null',"idBoard":"5fb51906cc7d395b1b145b0e","subscribed":'false'},
                                    {"id":"5fb51906cc7d395b1b145b11","name":"Done","closed":'false',"pos":49152,"softLimit":'null',"idBoard":"5fb51906cc7d395b1b145b0e","subscribed":'false'}
                                ]
                    }

    trello_cards = {"id":"5fb51906cc7d395b1b145b0e","name":"TO DO List",
                        "cards":[{"id":"5fb9923734e1420b507bc75e","checkItemStates":'null',"closed":'false',"dateLastActivity":"2020-11-23T22:49:51.032Z","desc":"Be able to display item's description","descData":{"emoji":{}},"dueReminder":'null',"idBoard":"5fb51906cc7d395b1b145b0e","idList":"5fb51906cc7d395b1b145b0f","idMembersVoted":[],"idShort":7,"idAttachmentCover":'null',"idLabels":[],"manualCoverAttachment":'false',"name":"Add item descriptions","pos":180223,"shortLink":"iZifatv8","isTemplate":'false',"cardRole":'null',"badges":{"attachmentsByType":{"trello":{"board":0,"card":0}},"location":'false',"votes":0,"viewingMemberVoted":'false',"subscribed":'false',"fogbugz":"","checkItems":0,"checkItemsChecked":0,"checkItemsEarliestDue":'null',"comments":0,"attachments":0,"description":'true',"due":'null',"dueComplete":'false',"start":'null'},"dueComplete":'false',"due":'null',"idChecklists":[],"idMembers":[],"labels":[],"shortUrl":"https://trello.com/c/iZifatv8","start":'null',"subscribed":'false',"url":"https://trello.com/c/iZifatv8/7-add-item-descriptions","cover":{"idAttachment":'null',"color":'null',"idUploadedBackground":'null',"size":"normal","brightness":"light"}},
                                    {"id":"5fb9924c9da5330af79e095c","checkItemStates":'null',"closed":'false',"dateLastActivity":"2020-11-21T22:18:53.003Z","desc":"","descData":'null',"dueReminder":'null',"idBoard":"5fb51906cc7d395b1b145b0e","idList":"5fb51906cc7d395b1b145b0f","idMembersVoted":[],"idShort":8,"idAttachmentCover":'null',"idLabels":[],"manualCoverAttachment":'false',"name":"Add due dates to items","pos":196607,"shortLink":"M9VpENnX","isTemplate":'false',"cardRole":'null',"badges":{"attachmentsByType":{"trello":{"board":0,"card":0}},"location":'false',"votes":0,"viewingMemberVoted":'false',"subscribed":'false',"fogbugz":"","checkItems":0,"checkItemsChecked":0,"checkItemsEarliestDue":'null',"comments":0,"attachments":0,"description":'false',"due":'null',"dueComplete":'false',"start":'null'},"dueComplete":'false',"due":'null',"idChecklists":[],"idMembers":[],"labels":[],"shortUrl":"https://trello.com/c/M9VpENnX","start":'null',"subscribed":'false',"url":"https://trello.com/c/M9VpENnX/8-add-due-dates-to-items","cover":{"idAttachment":'null',"color":'null',"idUploadedBackground":'null',"size":"normal","brightness":"light"}},
                                    {"id":"5fb51d88ee0bdc3d73b12727","checkItemStates":'null',"closed":'false',"dateLastActivity":"2020-11-23T22:34:55.578Z","desc":"","descData":'null',"dueReminder":'null',"idBoard":"5fb51906cc7d395b1b145b0e","idList":"5fb51906cc7d395b1b145b11","idMembersVoted":[],"idShort":1,"idAttachmentCover":'null',"idLabels":[],"manualCoverAttachment":'false',"name":"List saved todo items","pos":65535,"shortLink":"1pnzHzhm","isTemplate":'false',"cardRole":'null',"badges":{"attachmentsByType":{"trello":{"board":0,"card":0}},"location":'false',"votes":0,"viewingMemberVoted":'false',"subscribed":'false',"fogbugz":"","checkItems":0,"checkItemsChecked":0,"checkItemsEarliestDue":'null',"comments":0,"attachments":0,"description":'false',"due":'null',"dueComplete":'false',"start":'null'},"dueComplete":'false',"due":'null',"idChecklists":[],"idMembers":[],"labels":[],"shortUrl":"https://trello.com/c/1pnzHzhm","start":'null',"subscribed":'false',"url":"https://trello.com/c/1pnzHzhm/1-list-saved-todo-items","cover":{"idAttachment":'null',"color":'null',"idUploadedBackground":'null',"size":"normal","brightness":"light"}},
                                    {"id":"5fb51da7816eb055d84d36c7","checkItemStates":'null',"closed":'false',"dateLastActivity":"2020-11-21T22:19:00.803Z","desc":"","descData":'null',"dueReminder":'null',"idBoard":"5fb51906cc7d395b1b145b0e","idList":"5fb51906cc7d395b1b145b11","idMembersVoted":[],"idShort":2,"idAttachmentCover":'null',"idLabels":[],"manualCoverAttachment":'false',"name":"Allow new items to be added","pos":131071,"shortLink":"kH2cyNri","isTemplate":'false',"cardRole":'null',"badges":{"attachmentsByType":{"trello":{"board":0,"card":0}},"location":'false',"votes":0,"viewingMemberVoted":'false',"subscribed":'false',"fogbugz":"","checkItems":0,"checkItemsChecked":0,"checkItemsEarliestDue":'null',"comments":0,"attachments":0,"description":'false',"due":'null',"dueComplete":'false',"start":'null'},"dueComplete":'false',"due":'null',"idChecklists":[],"idMembers":[],"labels":[],"shortUrl":"https://trello.com/c/kH2cyNri","start":'null',"subscribed":'false',"url":"https://trello.com/c/kH2cyNri/2-allow-new-items-to-be-added","cover":{"idAttachment":'null',"color":'null',"idUploadedBackground":'null',"size":"normal","brightness":"light"}},
                                    {"id":"5fb6e1e82f69925fdacadae6","checkItemStates":'null',"closed":'false',"dateLastActivity":"2020-11-23T22:48:37.400Z","desc":"To be able to change status from Not Started to Completed and vice versa ","descData":{"emoji":{}},"dueReminder":'null',"idBoard":"5fb51906cc7d395b1b145b0e","idList":"5fb51906cc7d395b1b145b11","idMembersVoted":[],"idShort":3,"idAttachmentCover":'null',"idLabels":[],"manualCoverAttachment":'false',"name":"Change status of item","pos":147455,"shortLink":"SPuRBCNZ","isTemplate":'false',"cardRole":'null',"badges":{"attachmentsByType":{"trello":{"board":0,"card":0}},"location":'false',"votes":0,"viewingMemberVoted":'false',"subscribed":'false',"fogbugz":"","checkItems":0,"checkItemsChecked":0,"checkItemsEarliestDue":'null',"comments":0,"attachments":0,"description":'true',"due":'null',"dueComplete":'false',"start":'null'},"dueComplete":'false',"due":'null',"idChecklists":[],"idMembers":[],"labels":[],"shortUrl":"https://trello.com/c/SPuRBCNZ","start":'null',"subscribed":'false',"url":"https://trello.com/c/SPuRBCNZ/3-change-status-of-item","cover":{"idAttachment":'null',"color":'null',"idUploadedBackground":'null',"size":"normal","brightness":"light"}},
                                    {"id":"5fb7a65f82f5bf60c1d2623e","checkItemStates":'null',"closed":'false',"dateLastActivity":"2020-11-20T14:27:42.933Z","desc":"","descData":'null',"dueReminder":'null',"idBoard":"5fb51906cc7d395b1b145b0e","idList":"5fb51906cc7d395b1b145b11","idMembersVoted":[],"idShort":4,"idAttachmentCover":'null',"idLabels":[],"manualCoverAttachment":'false',"name":"Be able to delete item","pos":163839,"shortLink":"Xnz3mvPT","isTemplate":'false',"cardRole":'null',"badges":{"attachmentsByType":{"trello":{"board":0,"card":0}},"location":'false',"votes":0,"viewingMemberVoted":'false',"subscribed":'false',"fogbugz":"","checkItems":0,"checkItemsChecked":0,"checkItemsEarliestDue":'null',"comments":0,"attachments":0,"description":'false',"due":'null',"dueComplete":'false',"start":'null'},"dueComplete":'false',"due":'null',"idChecklists":[],"idMembers":[],"labels":[],"shortUrl":"https://trello.com/c/Xnz3mvPT","start":'null',"subscribed":'false',"url":"https://trello.com/c/Xnz3mvPT/4-be-able-to-delete-item","cover":{"idAttachment":'null',"color":'null',"idUploadedBackground":'null',"size":"normal","brightness":"light"}},
                                    {"id":"5fb9921fdded2e51055b7bf9","checkItemStates":'null',"closed":'false',"dateLastActivity":"2020-11-21T22:22:08.227Z","desc":"","descData":'null',"dueReminder":'null',"idBoard":"5fb51906cc7d395b1b145b0e","idList":"5fb51906cc7d395b1b145b11","idMembersVoted":[],"idShort":6,"idAttachmentCover":'null',"idLabels":[],"manualCoverAttachment":'false',"name":"Sort items by status","pos":163839,"shortLink":"IOYpwRya","isTemplate":'false',"cardRole":'null',"badges":{"attachmentsByType":{"trello":{"board":0,"card":0}},"location":'false',"votes":0,"viewingMemberVoted":'false',"subscribed":'false',"fogbugz":"","checkItems":0,"checkItemsChecked":0,"checkItemsEarliestDue":'null',"comments":0,"attachments":0,"description":'false',"due":'null',"dueComplete":'false',"start":'null'},"dueComplete":'false',"due":'null',"idChecklists":[],"idMembers":[],"labels":[],"shortUrl":"https://trello.com/c/IOYpwRya","start":'null',"subscribed":'false',"url":"https://trello.com/c/IOYpwRya/6-sort-items-by-status","cover":{"idAttachment":'null',"color":'null',"idUploadedBackground":'null',"size":"normal","brightness":"light"}}
                                ]
                    }


    trello_boards_response = MockedResponse(trello_boards)
    trello_cards_response = MockedResponse(trello_cards)
    
    @staticmethod
    def request(method, url, **kwargs):
        params = kwargs['params']

        if method == "GET":
            return MockedRequests.process_get_request(params)
        elif method == "POST":
            return MockedRequests.process_post_request(params)
        elif method == "DELETE":
            return MockedRequests.process_delete_request(params)
        else:
            """ method is PUT"""
            return MockedRequests.process_put_request(params)

    @staticmethod
    def process_get_request(params):
        if 'lists' in  params:
            return MockedRequests.trello_boards_response
        elif 'cards' in params:
            return MockedRequests.trello_cards_response
        else:
            return  {}

    @staticmethod
    def process_put_request(params):
        return MockedRequests.trello_cards_response       
    
    @staticmethod
    def process_post_request(params):
        return MockedRequests.trello_cards_response 

    @staticmethod
    def process_delete_request(params):
        return MockedRequests.trello_cards_response          
